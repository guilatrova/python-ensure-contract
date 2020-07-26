from abc import ABC, abstractmethod


class BaseNotification(ABC):
    """This base notificator removes any "badwords" and forwards
    the final message to somewhere.
    """
    def _treat_message(self, raw_message):
        return raw_message.replace("badword", "---")

    @abstractmethod
    def _emit_send_request(self, message):
        pass

    def send(self, raw_message):
        msg = self._treat_message(raw_message)
        return self._emit_send_request(msg)


class WhatsAppNotification(BaseNotification):
    """This notificator forwards messages through WhatsApp
    """
    def _emit_send_request(self, message):
        print("Sending notification through Whatsapp")
        return True


class EmailNotification(BaseNotification):
    """This notificator forwards messages through E-mail
    """

    def _emit_send_request(self, msg):
        print("Sending notification through Email")
        return True


class TelegramNotification(BaseNotification):
    """This notificator breaks because it's not
    compatible with BaseNotification contract
    """

    def notificate(self, msg):
        print("Not respecting contract")
