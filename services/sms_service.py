from services.notification_service import NotificationService


class SmsService(NotificationService):
    def send(self, to: str, message: str) -> None:
        # TODO (à faire):
        # - Afficher une notification SMS
        print(f"[SMS] to={to} msg={message}")
