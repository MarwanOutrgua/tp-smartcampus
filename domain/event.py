from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from domain.club import Club
    from domain.registration import Registration

from domain.student import Student

class Event:
    """Événement organisé par un club (association 1–N).

    L'événement conserve une liste d'inscriptions (Registration) :
    - cela matérialise la relation N–N Student <-> Event via la classe d'association.
    """

    def __init__(self, event_id: int, title: str, date: str, capacity: int, club: "Club"):
        # TODO (à faire):
        # 1) Initialiser l'id (entier > 0)
        self.id = event_id
        # 2) Initialiser les champs simples (validés dans setters)
        self.title = title        # non vide
        self.date = date          # non vide
        self.capacity = capacity  # > 0
        # 3) Initialiser le club (doit être Club)
        self.club = club
        # 4) Initialiser la liste d'inscriptions
        self._registrations = []
        # 5) Rattacher l'événement au club
        self.club._add_event(self)

    @property
    def id(self) -> int:
        # TODO: retourner _id
        return self._id

    @id.setter
    def id(self, value: int) -> None:
        # TODO:
        v = int(value)
        # - vérifier v > 0
        if v > 0:
            self._id = v
        else:
            raise Exception("id doit etre superieur à 0")

    @property
    def title(self) -> str:
        # TODO: retourner _title
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        # TODO:
        v = str(value).strip()
        # - vérifier non vide
        if v == "":
            raise Exception("le nom ne doit pas etre vide")
        self._title = v

    @property
    def date(self) -> str:
        # TODO: retourner _date
        return self._date

    @date.setter
    def date(self, value: str) -> None:
        # TODO:
        v = str(value).strip()
        # - vérifier non vide
        if v != "":
            self._date = v
        else:
            raise Exception("la date ne doit pas etre vide")

    @property
    def capacity(self) -> int:
        # TODO: retourner _capacity
        return self._capacity

    @capacity.setter
    def capacity(self, value: int) -> None:
        # TODO:
        v = int(value)
        # - vérifier v > 0
        if v > 0:
            self._capacity = v
        else:
            raise Exception("la capacite doit etre supérieur à 0")

    @property
    def club(self) -> "Club":
        # TODO: retourner _club
        return self._club

    @club.setter
    def club(self, value: "Club") -> None:
        # TODO:
        # - vérifier isinstance(value, Club)
        # - sinon TypeError
        if not isinstance(value, object):  # At runtime, use object check
            raise TypeError(
                "La valeur fournie doit être une instance de la classe Club.")
        self._club = value

    def is_full(self) -> bool:
        # TODO (à faire):
        # - Compter uniquement les inscriptions dont status == "CONFIRMED"
        confirmed_count = sum(
            1 for reg in self._registrations if reg.status == "CONFIRMED")
        # - Retourner True si confirmed >= capacity, sinon False
        return confirmed_count >= self.capacity

    def add_registration(self, student: Student, reg: "Registration") -> None:
        # TODO (à faire):
        # - Éviter le doublon pour un même student.id
        for existing_student in self._registrations:
            if existing_student.student.id == student.id:
                print(f"L'étudiant {student.id} est déjà présent.")
                return
        # - Si pas déjà inscrit: self._registrations.append(reg)
        self._registrations.append(reg)

    def find_registration(self, student_id: int) -> "Registration | None":
        # TODO (à faire):
        # - Parcourir _registrations et retourner celle dont reg.student.id == student_id
        for reg in self._registrations:
            if reg.student.id == student_id:
                return reg
        # - Sinon None
        return None

    def list_registrations(self) -> list["Registration"]:
        # TODO: retourner copie
        return list(self._registrations)

    def __str__(self) -> str:
        # TODO:
        # - Calculer nb confirmed
        confirmed_count = sum(
            1 for reg in self._registrations if reg.status == "CONFIRMED")
        return f"Event(id={self.id}, title={self.title}, date={self.date}, cap={self.capacity}, confirmed={confirmed_count}, club={self.club.name})"