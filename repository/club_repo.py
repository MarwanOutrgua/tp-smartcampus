from domain.club import Club


class ClubRepository:
    def __init__(self):
        self._data: dict[int, Club] = {}

    def add(self, club: Club) -> None:
        # TODO:
        # - Vérifier type Club
        if not isinstance(club, Club):
            raise TypeError(
                f"Attendu : instance de Club, reçu : {type(club).__name__}")
        # - Refuser doublon (club.id)
        for c in self._data:
            if c == club.id:
                return
        # - Stocker
        self._data[club.id] = club

    def get_by_id(self, club_id: int) -> Club | None:
        # TODO:
        return self._data.get(int(club_id))

    def list_all(self) -> list[Club]:
        # TODO:
        return list(self._data.values())
