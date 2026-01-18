from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from domain.event import Event

from domain.student import Student

class Club:
    """Club étudiant.

    Relations:
    - Agrégation: contient des membres (Student) sans les "posséder" (ils vivent indépendamment)
    - Association 1–N: possède des événements (Event) liés à ce club
    """

    def __init__(self, club_id: int, name: str):
        # TODO (à faire):
        # 1) Initialiser l'identifiant (entier > 0)
        self.id = club_id
        # 2) Initialiser le nom (non vide)
        self.name = name
        # 3) Initialiser les collections
        self._members: list[Student] = []
        self._events: list[Event] = []

    @property
    def id(self) -> int:
        # TODO: retourner _id
        return self._id

    @id.setter
    def id(self, value: int) -> None:
        # TODO:
        v = int(value)
        if v > 0:
            self._id = v
        else:
            raise Exception("id doit etre superieur à 0")

    @property
    def name(self) -> str:
        # TODO: retourner _name
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        # TODO:
        v = str(value).strip()
        # - vérifier non vide, sinon ValueError
        if v != "":
            self._name = v
        else:
            raise Exception("le nom ne doit pas etre vide")

    def add_member(self, student: Student) -> None:
        # TODO (à faire):
        # - Vérifier type:
        #   - si student n'est pas Student -> TypeError
        if not isinstance(student, Student):
            raise TypeError(
                "L'objet ajouté doit être une instance de la classe Student.")
        # - Éviter les doublons (même id):
        #   - si déjà présent -> ne rien faire (return)
        for s in self._members:
            if s.id == student.id:
                return
        self._members.append(student)

    def remove_member(self, student_id: int) -> Student | None:
        # TODO (à faire):
        # - Convertir student_id en int
        student_id = int(student_id)
        # - Parcourir self._members pour trouver un Student ayant s.id == student_id
        # - Si trouvé: le retirer de la liste et le retourner
        # - Sinon: retourner None
        for i, s in enumerate(self._members):
            if s.id == student_id:
                # .pop(i) retire l'élément à l'index i et le renvoie
                return self._members.pop(i)
        return None

    def list_members(self) -> list[Student]:
        # TODO: retourner une copie (list(self._members)) pour éviter la modification externe
        return list(self._members)

    def _add_event(self, event: "Event") -> None:
        # TODO (à faire):
        # - Méthode interne (usage par Event)
        # - Ajouter event à self._events si absent
        if event not in self._events:
            self._events.append(event)

    def list_events(self) -> list["Event"]:
        # TODO: retourner copie de la liste d'événements
        return list(self._events)

    def __str__(self) -> str:
        # TODO:
        return f"id = {self._id} , name = {self._name} , members = {self._members} , events = {self._events}"