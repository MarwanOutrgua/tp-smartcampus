from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from domain.event import Event

from domain.student import Student

class Registration:
    """Classe d'association (N–N) entre Student et Event.

    Attributs supplémentaires:
    - date_inscription
    - status (CONFIRMED/CANCELLED)
    - present (bool | None)
    """

    STATUS_CONFIRMED = "CONFIRMED"
    STATUS_CANCELLED = "CANCELLED"

    def __init__(self, student: Student, event: "Event", date_inscription: str):
        # TODO (à faire):
        # 1) Initialiser student et event (types corrects)
        self.student = student
        self.event = event
        # 2) Initialiser date_inscription (non vide)
        self.date_inscription = date_inscription
        # 3) Initialiser status à CONFIRMED
        self.status = self.STATUS_CONFIRMED
        # 4) Initialiser present à None (pas encore marqué)
        self.present = None
        

    @property
    def student(self) -> Student:
        # TODO: retourner _student
        return self._student

    @student.setter
    def student(self, value: Student) -> None:
        # TODO:
        # - vérifier isinstance(value, Student)
        # - sinon TypeError
        if not isinstance(value, Student):
          raise TypeError(f"Attendu: instance de Student, reçu: {type(value).__name__}")
        self._student = value

    @property
    def event(self) -> "Event":
        # TODO: retourner _event
        return self._event

    @event.setter
    def event(self, value: "Event") -> None:
        # TODO:
        # - vérifier isinstance(value, Event)
        # - sinon TypeError
        if not isinstance(value, object):  # At runtime, use object check since we can't import Event
          raise TypeError(f"Attendu: instance de Event, reçu: {type(value).__name__}")
        self._event = value

    @property
    def date_inscription(self) -> str:
        # TODO: retourner _date_inscription
        return self._date_inscription

    @date_inscription.setter
    def date_inscription(self, value: str) -> None:
        # TODO:
        v = str(value).strip()
        # - vérifier non vide
        if v != "" :
          self._date_inscription = v
        else:
            raise Exception("la date inscription ne doit pas etre vide")

    @property
    def status(self) -> str:
        # TODO: retourner _status
        return self._status

    @status.setter
    def status(self, value: str) -> None:
        # TODO:
        v = str(value).strip().upper()
        # - vérifier v in (CONFIRMED, CANCELLED)
        if v in ("CONFIRMED", "CANCELLED"):
         self._status = v
        else:
           raise ValueError("Le statut doit être 'CONFIRMED' ou 'CANCELLED'")
        
    def cancel(self) -> None:
        # TODO:
        # - Passer l'inscription en CANCELLED
        self.status = Registration.STATUS_CANCELLED

    def mark_presence(self, present: bool) -> None:
        # TODO:
        # - Interdire si status != CONFIRMED (lever ValueError)
        if self.status != "CONFIRMED":
          raise ValueError(f"Impossible de marquer la présence : le statut est '{self.status}' au lieu de 'CONFIRMED'.")
        # - Sinon: self.present = bool(present)
        self.present = bool(present)

    def __str__(self) -> str:
        # TODO:
        return f"student = {self._student} , event = {self._event} , status = {self._status} , present = {self.present}"