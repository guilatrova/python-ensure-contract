class CronJob:
    def __init__(self, notificator):
        self.notificator = notificator

    def execute(self):
        print("Executing cron job")
        notification_emitted = self.notificator.send("Job has been executed")
        if not notification_emitted:
            raise Exception("Notification failed")
