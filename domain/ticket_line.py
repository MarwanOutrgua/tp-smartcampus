class TicketLine:
    """Ligne de billet (fait partie d'une commande: composition)."""

    def __init__(self, label: str, quantity: int, unit_price: float):
        # TODO (à faire):
        # - Initialiser les champs via setters (validations)
        self.label = label
        self.quantity = quantity
        self.unit_price = unit_price

    @property
    def label(self) -> str:
        # TODO: retourner _label
        return self._label

    @label.setter
    def label(self, value: str) -> None:
        # TODO:
        v = str(value).strip()
        # - vérifier non vide
        if v == "":
            raise Exception("label ne doit pas etre vide")
        self._label = v

    @property
    def quantity(self) -> int:
        # TODO: retourner _quantity
        return self._quantity

    @quantity.setter
    def quantity(self, value: int) -> None:
        # TODO:
        v = int(value)
        # - vérifier v > 0
        if v <= 0:
            raise Exception("quantite doit etre supérieur à 0")
        self._quantity = v

    @property
    def unit_price(self) -> float:
        # TODO: retourner _unit_price
        return self._unit_price

    @unit_price.setter
    def unit_price(self, value: float) -> None:
        # TODO:
        v = float(value)
        # - vérifier v > 0
        if v <= 0:
            raise Exception("unit price doit etre supérieur à 0")
        self._unit_price = v

    def subtotal(self) -> float:
        # TODO:
        # - Retourner quantity * unit_price
        return self.quantity * self.unit_price

    def __str__(self) -> str:
        # TODO:
        return f"label : {self._label} , quantity : {self._quantity} ,unit : {self._unit_price} , subtotal : {self.subtotal():.2f}$"