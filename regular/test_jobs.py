from unittest.mock import patch
import pytest
import notifications
from jobs import CronJob


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


class TestBrokenContract:
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
