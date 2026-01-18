from domain.event import Event


class EventRepository:
    def __init__(self):
        self._data: dict[int, Event] = {}

    def add(self, event: Event) -> None:
        # TODO:
        # - Vérifier type Event
        if not isinstance(event, Event):
            raise TypeError(
                f"Attendu : instance de Event, reçu : {type(event).__name__}")
        # - Refuser doublon (event.id)
        for e in self._data:
            if e == event.id:
                return
        # - Stocker
        self._data[event.id] = event

    def get_by_id(self, event_id: int) -> Event | None:
        # TODO:
        return self._data.get(int(event_id))

    def list_all(self) -> list[Event]:
        # TODO:
        return list(self._data.values())

    def list_by_club(self, club_id: int) -> list[Event]:
        # TODO:
        cid = int(club_id)
        # - retourner les events dont e.club.id == cid
        return [e for e in self._data.values() if e.club and e.club.id == cid]
