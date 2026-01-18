from domain.profile import Profile
from domain.student import Student
from domain.club import Club
from domain.event import Event
from domain.registration import Registration
from domain.ticket_order import TicketOrder

from repository.student_repo import StudentRepository
from repository.club_repo import ClubRepository
from repository.event_repo import EventRepository
from repository.order_repo import OrderRepository

from services.notification_service import NotificationService


class CampusService:
    """Couche service: cas d'usage + règles métier."""

    def __init__(self):
        self.students = StudentRepository()
        self.clubs = ClubRepository()
        self.events = EventRepository()
        self.orders = OrderRepository()

        # Compteurs simples pour générer des IDs en mémoire
        self._next_student_id = 1
        self._next_club_id = 1
        self._next_event_id = 1
        self._next_order_id = 1

    # Règles métier Student
    # -------------------------
    def create_student(self, name: str, bio: str, email: str, phone: str) -> Student:
        profile = Profile(bio, email, phone)
        student = Student(self._next_student_id, name, profile)
        self.students.add(student)
        self._next_student_id += 1
        return student

    def list_students(self) -> list[Student]:
        return self.students.list_all()

    # Règles métier Club
    # -------------------------

    def create_club(self, name: str) -> Club:
        club = Club(self._next_club_id, name)
        self.clubs.add(club)
        self._next_club_id += 1
        return club

    def list_clubs(self) -> list[Club]:
        return self.clubs.list_all()

    def add_member_to_club(self, club_id: int, student_id: int) -> None:
        # Récupérer le club
        club = self.clubs.get_by_id(club_id)
        if club is None:
            raise ValueError(f"Club introuvable avec l'ID : {club_id}")
        
        # Récupérer l'étudiant
        student = self.students.get_by_id(student_id)
        if student is None:
            raise ValueError(f"Étudiant introuvable avec l'ID : {student_id}")
        
        # Ajouter le membre
        club.add_member(student)

    def remove_member_from_club(self, club_id: int, student_id: int) -> None:
        # Récupérer club
        club = self.clubs.get_by_id(club_id)
        if club is None:
            raise ValueError(f"Club introuvable avec l'ID : {club_id}")
        
        removed = club.remove_member(student_id)
        # Si removed est None: ValueError
        if removed is None:
            raise ValueError(
                f"L'étudiant avec l'ID {student_id} est introuvable dans le club {club.name}.")
        return removed

    # Règles métier Event
    # -------------------------
    def create_event(self, club_id: int, title: str, date: str, capacity: int) -> Event:
        # Récupérer club
        club = self.clubs.get_by_id(club_id)
        if club is None:
            raise ValueError(
                f"Erreur : Le club avec l'ID {club_id} n'existe pas dans le système.")
        
        event = Event(self._next_event_id, title, date, capacity, club)
        self.events.add(event)
        self._next_event_id += 1
        return event

    def list_events_by_club(self, club_id: int) -> list[Event]:
        # Vérifier club existe
        club = self.clubs.get_by_id(club_id)
        if club is None:
            raise ValueError(
                f"Action impossible : le club {club_id} n'existe pas.")
        
        # Retourner les événements du club
        return club.list_events()

    # Règles métier Registration
    # -------------------------
    def register_student(
        self,
        student_id: int,
        event_id: int,
        date_inscription: str,
        notifier: NotificationService | None = None
    ) -> Registration:
        # Charger student et event
        student = self.students.get_by_id(student_id)
        if not student:
            raise ValueError(
                f"Échec du chargement : l'étudiant {student_id} n'existe pas.")
        
        event = self.events.get_by_id(event_id)
        if not event:
            raise ValueError(
                f"Échec du chargement : l'événement {event_id} n'existe pas.")
        
        # Refuser inscription si déjà CONFIRMED
        existing = event.find_registration(student_id)
        if existing is not None:
            raise ValueError(
                f"L'étudiant {student_id} est déjà inscrit à cet événement.")
        
        # Refuser si event complet
        if event.is_full():
            raise ValueError(
                f"Impossible de s'inscrire : l'événement '{event.title}' a déjà atteint sa capacité maximale de {event.capacity} places.")
        
        # Créer Registration et l'ajouter à l'event
        reg = Registration(student, event, date_inscription)
        event.add_registration(student, reg)
        
        # Dépendance (notification):
        if notifier is not None:
            message = f"Félicitations {student.name}, votre inscription à l'événement '{event.title}' est confirmée !"
            notifier.send(student.profile.email, message)
        
        return reg

    def cancel_registration(self, student_id: int, event_id: int) -> None:
        # Récupération de l'événement
        event = self.events.get_by_id(event_id)
        if event is None:
            raise ValueError(
                f"Échec de l'opération : aucun événement trouvé avec l'ID {event_id}.")
        
        # Rechercher l'inscription dans l'événement
        reg = event.find_registration(student_id)
        if reg is None:
            raise ValueError(
                f"Impossible d'annuler : l'étudiant {student_id} n'est pas inscrit à l'événement '{event.title}'.")
        
        # Appeler la méthode d'annulation
        reg.cancel()

    def mark_presence(self, student_id: int, event_id: int, present: bool) -> None:
        # Récupération de l'événement
        event = self.events.get_by_id(event_id)
        if event is None:
            raise ValueError(
                f"Échec de l'opération : aucun événement trouvé avec l'ID {event_id}.")
        
        # Rechercher l'inscription
        reg = event.find_registration(student_id)
        if reg is None:
            raise ValueError(
                f"L'étudiant {student_id} n'est pas inscrit à l'événement {event_id}.")
        
        # Marquer la présence
        try:
            reg.mark_presence(present)
        except ValueError as e:
            raise ValueError(f"Action refusée : {e}")

    # Règles métier Order
    # -------------------------
    def create_order(self, student_id: int) -> TicketOrder:
        # Vérifier student existe
        student = self.students.get_by_id(student_id)
        if student is None:
            raise ValueError(
                f"L'étudiant avec l'ID {student_id} est introuvable.")
        
        order = TicketOrder(self._next_order_id, student_id)
        self.orders.add(order)
        self._next_order_id += 1
        return order

    def add_ticket_line(self, order_id: int, label: str, quantity: int, unit_price: float) -> None:
        # Retrouver order
        order = self.orders.get_by_id(order_id)
        if order is None:
            raise ValueError(
                f"Impossible d'ajouter une ligne : la commande ID {order_id} n'existe pas.")
        order.add_line(label, quantity, unit_price)

    def checkout(self, order_id: int) -> float:
        # Retrouver order
        order = self.orders.get_by_id(order_id)
        if order is None:
            raise ValueError(
                f"Erreur de facturation : la commande '{order_id}' est introuvable.")
        
        total = order.total()
        
        # Afficher un reçu simple
        print("\n" + "="*30)
        print(f"      REÇU DE COMMANDE")
        print("="*30)
        print(f"ID Commande : {order.id}")
        print("-" * 30)
        print(f"TOTAL À PAYER : {total:.2f}€")
        print("="*30 + "\n")
        
        return total