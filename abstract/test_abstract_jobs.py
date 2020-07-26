from unittest.mock import patch
import pytest
import abs_notifications as notifications
from jobs import CronJob


@pytest.mark.parametrize("notificator_cls", [
    notifications.WhatsAppNotification,
    notifications.EmailNotification
])
class TestNotificator:
    """Intentionally parametrize only 2 valid notification implementations.
    If we've tested Telegram here we would find a failure that would help us
    identifying that Telegram is not respecting its contract :)
    """

    def test_notificator_treats_bad_words(self, notificator_cls):
        notificator = notificator_cls()
        with patch.object(notificator, "_emit_send_request") as send_mock:
            notificator.send("test badword filter from base class")
            send_mock.assert_called_once_with("test --- filter from base class")


class TestValidContract:
    """Test job dependency with different implementations
    """
    def test_job_notificates_through_whatsapp(self):
        job = CronJob(notifications.WhatsAppNotification())
        job.execute()

    def test_job_notificates_through_email(self):
        job = CronJob(notifications.EmailNotification())
        job.execute()

    def test_job_throws_exception_when_notification_fails(self):
        """Mocks notificator to return False
        """
        notificator = notifications.WhatsAppNotification()
        with patch.object(notificator, "send", return_value=False):
            with pytest.raises(Exception):
                job = CronJob(notificator)
                job.execute()


class TestAbstractBrokenContract:
    """Suite of tests that prove Telegram is not respecting
    its contract.
    """

    def test_telegram_throws_exception_when_notification_fails(self):
        """Mocking notificator does not fix a broken
        contract
        """
        notificator = notifications.TelegramNotification()
        with patch.object(notificator, "send", return_value=False):
            with pytest.raises(Exception):
                job = CronJob(notificator)
                job.execute()

    def test_job_notificates_through_telegram(self):
        """This test will fail because
        Telegram implementation does not respect contract
        """
        job = CronJob(notifications.TelegramNotification())
        job.execute()
