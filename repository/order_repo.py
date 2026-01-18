from domain.ticket_order import TicketOrder


class OrderRepository:
    def __init__(self):
        self._data: dict[int, TicketOrder] = {}

    def add(self, order: TicketOrder) -> None:
        # TODO:
        # - Vérifier type TicketOrder
        if not isinstance(order, TicketOrder):
            raise TypeError(
                f"Attendu : instance de TicketOrder, reçu : {type(order).__name__}")
        # - Refuser doublon (order.id)
        for o in self._data:
            if o == order.id:
                return
        # - Stocker
        self._data[order.id] = order

    def get_by_id(self, order_id: int) -> TicketOrder | None:
        # TODO:
        # - return self._data.get(int(order_id))
        return self._data.get(int(order_id))

    def list_all(self) -> list[TicketOrder]:
        # TODO:
        # - return list(self._data.values())
        return list(self._data.values())
