import customtkinter as ctk
from tkinter import messagebox, simpledialog
from services.campus_service import CampusService
from services.email_service import EmailService
from services.sms_service import SmsService
from datetime import datetime

# Configuration du thème
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class Menu(ctk.CTk):
    """UI Graphique avec CustomTkinter."""

    def __init__(self):
        super().__init__()
        self.service = CampusService()
        self.email_service = EmailService()
        self.sms_service = SmsService()
        
        # Configuration de la fenêtre
        self.title("SmartCampus - Management System")
        self.geometry("1100x700")

        # Configuration de la grille (2 colonnes, 1 ligne)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # --- BARRE LATÉRALE (SIDEBAR) ---
        self.sidebar_frame = ctk.CTkFrame(self, width=250, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="SmartCampus", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.pack(pady=20, padx=10)

        # Boutons du menu
        self._create_menu_buttons()

        # --- ZONE CENTRALE (CONTENU) ---
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        
        self.title_label = ctk.CTkLabel(self.main_frame, text="Sélectionnez une action dans le menu", font=ctk.CTkFont(size=16))
        self.title_label.pack(pady=10)

        # Zone de log (console-like)
        self.console_output = ctk.CTkTextbox(self.main_frame, width=700, height=400)
        self.console_output.pack(padx=20, pady=20, expand=True, fill="both")

    def _create_menu_buttons(self):
        """Crée dynamiquement les boutons du menu."""
        options = [
            ("1) Ajouter étudiant", self._ui_add_student),
            ("2) Lister étudiants", self._ui_list_students),
            ("3) Créer club", self._ui_create_club),
            ("4) Lister clubs", self._ui_list_clubs),
            ("5) Ajouter membre à club", self._ui_add_member_to_club),
            ("6) Créer événement", self._ui_create_event),
            ("7) Lister événements", self._ui_list_events),
            ("8) Inscrire à événement", self._ui_register_student),
            ("9) Annuler inscription", self._ui_cancel_registration),
            ("10) Marquer présence", self._ui_mark_presence),
            ("11) Billetterie", self._ui_billing),
            ("0) Quitter", self.quit)
        ]
        
        for text, command in options:
            btn = ctk.CTkButton(self.sidebar_frame, text=text, command=command, font=ctk.CTkFont(size=11))
            btn.pack(pady=3, padx=10, fill="x")

    # --- MÉTHODES D'ACTIONS (LOGIQUE UI) ---

    def _log(self, message):
        """Affiche un message dans la zone de texte centrale."""
        self.console_output.insert("end", f"> {message}\n")
        self.console_output.see("end")

    def _input_dialog(self, title, prompt):
        """Helper pour demander une saisie à l'utilisateur."""
        dialog = ctk.CTkInputDialog(text=prompt, title=title)
        return dialog.get_input()

    # 1) Ajouter étudiant
    def _ui_add_student(self):
        """Ajoute un étudiant avec profil."""
        name = self._input_dialog("Nouvel Étudiant", "Nom :")
        if not name:
            return
        
        bio = self._input_dialog("Profil", "Biographie :")
        if not bio:
            bio = "N/A"
        
        email = self._input_dialog("Profil", "Email :")
        if not email:
            self._log("✗ Email requis")
            return
        
        phone = self._input_dialog("Profil", "Téléphone :")
        if not phone:
            phone = "N/A"
        
        try:
            student = self.service.create_student(name, bio, email, phone)
            self._log(f"✓ Étudiant créé : ID={student.id}, Nom={name}")
        except Exception as e:
            self._log(f"✗ Erreur : {e}")
            messagebox.showerror("Erreur", str(e))

    # 2) Lister étudiants
    def _ui_list_students(self):
        """Affiche la liste des étudiants."""
        try:
            students = self.service.list_students()
            if not students:
                self._log("Aucun étudiant enregistré.")
            else:
                self._log("=== LISTE DES ÉTUDIANTS ===")
                for s in students:
                    self._log(f"  ID: {s.id} | Nom: {s.name} | Email: {s.profile.email}")
        except Exception as e:
            self._log(f"✗ Erreur : {e}")

    # 3) Créer club
    def _ui_create_club(self):
        """Crée un nouveau club."""
        name = self._input_dialog("Nouveau Club", "Nom du club :")
        if not name:
            return
        
        try:
            club = self.service.create_club(name)
            self._log(f"✓ Club créé : ID={club.id}, Nom={name}")
        except Exception as e:
            self._log(f"✗ Erreur : {e}")
            messagebox.showerror("Erreur", str(e))

    # 4) Lister clubs
    def _ui_list_clubs(self):
        """Affiche la liste des clubs."""
        try:
            clubs = self.service.list_clubs()
            if not clubs:
                self._log("Aucun club enregistré.")
            else:
                self._log("=== LISTE DES CLUBS ===")
                for c in clubs:
                    self._log(f"  ID: {c.id} | Nom: {c.name} | Membres: {len(c.list_members())}")
        except Exception as e:
            self._log(f"✗ Erreur : {e}")

    # 5) Ajouter membre à un club
    def _ui_add_member_to_club(self):
        """Ajoute un étudiant à un club."""
        club_id = self._input_dialog("Ajouter membre", "ID du club :")
        if not club_id:
            return
        
        student_id = self._input_dialog("Ajouter membre", "ID de l'étudiant :")
        if not student_id:
            return
        
        try:
            self.service.add_member_to_club(int(club_id), int(student_id))
            self._log(f"✓ Étudiant {student_id} ajouté au club {club_id}")
        except Exception as e:
            self._log(f"✗ Erreur : {e}")
            messagebox.showerror("Erreur", str(e))

    # 6) Créer événement
    def _ui_create_event(self):
        """Crée un événement pour un club."""
        club_id = self._input_dialog("Nouvel Événement", "ID du club :")
        if not club_id:
            return
        
        title = self._input_dialog("Nouvel Événement", "Titre de l'événement :")
        if not title:
            return
        
        date = self._input_dialog("Nouvel Événement", "Date (YYYY-MM-DD) :")
        if not date:
            return
        
        capacity = self._input_dialog("Nouvel Événement", "Capacité (nombre) :")
        if not capacity:
            return
        
        try:
            event = self.service.create_event(int(club_id), title, date, int(capacity))
            self._log(f"✓ Événement créé : ID={event.id}, Titre={title}, Capacité={capacity}")
        except Exception as e:
            self._log(f"✗ Erreur : {e}")
            messagebox.showerror("Erreur", str(e))

    # 7) Lister événements
    def _ui_list_events(self):
        """Liste les événements d'un club."""
        club_id = self._input_dialog("Lister événements", "ID du club :")
        if not club_id:
            return
        
        try:
            events = self.service.list_events_by_club(int(club_id))
            if not events:
                self._log(f"Aucun événement pour le club {club_id}")
            else:
                self._log(f"=== ÉVÉNEMENTS DU CLUB {club_id} ===")
                for e in events:
                    self._log(f"  ID: {e.id} | Titre: {e.title} | Date: {e.date} | Capacité: {e.capacity}")
        except Exception as e:
            self._log(f"✗ Erreur : {e}")

    # 8) Inscrire étudiant à événement
    def _ui_register_student(self):
        """Inscrit un étudiant à un événement."""
        student_id = self._input_dialog("Inscription", "ID de l'étudiant :")
        if not student_id:
            return
        
        event_id = self._input_dialog("Inscription", "ID de l'événement :")
        if not event_id:
            return
        
        try:
            date_inscription = datetime.now().strftime("%Y-%m-%d")
            reg = self.service.register_student(int(student_id), int(event_id), date_inscription, self.email_service)
            self._log(f"✓ Étudiant {student_id} inscrit à l'événement {event_id}")
            self._log(f"  Notification Email envoyée")
        except Exception as e:
            self._log(f"✗ Erreur : {e}")
            messagebox.showerror("Erreur", str(e))

    # 9) Annuler inscription
    def _ui_cancel_registration(self):
        """Annule l'inscription d'un étudiant."""
        student_id = self._input_dialog("Annuler inscription", "ID de l'étudiant :")
        if not student_id:
            return
        
        event_id = self._input_dialog("Annuler inscription", "ID de l'événement :")
        if not event_id:
            return
        
        try:
            self.service.cancel_registration(int(student_id), int(event_id))
            self._log(f"✓ Inscription annulée pour étudiant {student_id}, événement {event_id}")
        except Exception as e:
            self._log(f"✗ Erreur : {e}")
            messagebox.showerror("Erreur", str(e))

    # 10) Marquer présence
    def _ui_mark_presence(self):
        """Marque la présence d'un étudiant."""
        student_id = self._input_dialog("Marquer présence", "ID de l'étudiant :")
        if not student_id:
            return
        
        event_id = self._input_dialog("Marquer présence", "ID de l'événement :")
        if not event_id:
            return
        
        present = messagebox.askyesno("Marquer présence", "Étudiant présent ?")
        
        try:
            self.service.mark_presence(int(student_id), int(event_id), present)
            status = "Présent" if present else "Absent"
            self._log(f"✓ Présence marquée : Étudiant {student_id} - {status}")
        except Exception as e:
            self._log(f"✗ Erreur : {e}")
            messagebox.showerror("Erreur", str(e))

    # 11) Billetterie
    def _ui_billing(self):
        """Gère les commandes de billets."""
        student_id = self._input_dialog("Billetterie", "ID de l'étudiant :")
        if not student_id:
            return
        
        try:
            order = self.service.create_order(int(student_id))
            self._log(f"✓ Commande créée : ID={order.id}")
            
            # Ajouter des lignes
            while True:
                label = self._input_dialog("Ajouter ligne", "Libellé du billet (ou vide pour terminer) :")
                if not label:
                    break
                
                quantity = self._input_dialog("Ajouter ligne", "Quantité :")
                if not quantity:
                    continue
                
                price = self._input_dialog("Ajouter ligne", "Prix unitaire :")
                if not price:
                    continue
                
                try:
                    self.service.add_ticket_line(order.id, label, int(quantity), float(price))
                    self._log(f"  + {label} x{quantity} @ {price}€")
                except Exception as e:
                    self._log(f"  ✗ Erreur : {e}")
            
            # Checkout
            total = self.service.checkout(order.id)
            self._log(f"✓ Total à payer : {total:.2f}€")
        except Exception as e:
            self._log(f"✗ Erreur : {e}")
            messagebox.showerror("Erreur", str(e))

    def run(self):
        """Lance l'application."""
        self.mainloop()

# --- POINT D'ENTRÉE ---
if __name__ == "__main__":
    app = Menu()
    app.run()