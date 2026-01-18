from domain.ticket_line import TicketLine


class TicketOrder:
    """Commande de billets (composition avec TicketLine).

    Composition: les TicketLine n'existent que dans la commande.
    """

    def __init__(self, order_id: int, student_id: int):
        # TODO (à faire):
        # 1) Initialiser id et student_id (entiers > 0)
        self.id = order_id
        self.student_id = student_id
        # 2) Initialiser la liste des lignes
        self._lines = []

    @property
    def id(self) -> int:
        # TODO: retourner _id
        return self._id

    @id.setter
    def id(self, value: int) -> None:
        # TODO:
        v = int(value)
        # - vérifier v > 0
        if v <= 0:
            raise Exception("id order doit etre superieur à 0")
        self._id = v

    @property
    def student_id(self) -> int:
        # TODO: retourner _student_id
        return self._student_id

    @student_id.setter
    def student_id(self, value: int) -> None:
        # TODO:
        v = int(value)
        # - vérifier v > 0
        if v <= 0:
            raise Exception("id student doit etre supérieur à 0")
        self._student_id = v

    def add_line(self, label: str, quantity: int, unit_price: float) -> None:
        # TODO (à faire):
        # - Créer une ligne
        line = TicketLine(label, quantity, unit_price)
        # - L'ajouter à self._lines
        self._lines.append(line)

    def total(self) -> float:
        # TODO:
        # - Retourner la somme des sous-totaux des lignes
        return sum(line.subtotal() for line in self._lines)

    def list_lines(self) -> list[TicketLine]:
        # TODO: retourner copie
        return list(self._lines)

    def __str__(self) -> str:
        # TODO:
        return f"id = {self._id} , student = {self._student_id} , lines = {self._lines} , total = {self.total():.2f}$"