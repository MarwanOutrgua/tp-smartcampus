from services.notification_service import NotificationService


class EmailService(NotificationService):
    def send(self, to: str, message: str) -> None:
        # TODO (à faire):
        # - Afficher une notification Email
        print(f"[EMAIL] to={to} msg={message}")
