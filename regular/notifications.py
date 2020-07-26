class WhatsAppNotification:
    def send(self, msg):
        print("Sending notification through Whatsapp")
        return True


class EmailNotification:
    def send(self, msg):
        print("Sending notification through Email")
        return True


class TelegramNotification:
    def notificate(self, msg):
        print("Not respecting contract")
