from django.test import TestCase
from datetime import datetime, timezone
from django.core.exceptions import ValidationError
from forum_app import models

THREAD = {"title": "test_thread"}
SECTION = {"name": "test_section"}
USER = {"username": "test_username", "password": "test_Password112233"}
MESSAGE = {"message_body": "some message"}


class TestLinks(TestCase):
    def test_thread_section(self):
        thread = models.Thread.objects.create(**THREAD)
        section = models.Section.objects.create(**SECTION)
        thread.save()
        thread.sections.add(section.id)
        thread_section_link = models.SectionThread.objects.filter(thread=thread, section=section)
        self.assertEqual(len(thread_section_link), 1)

    def test_user_thread(self):
        thread = models.Thread.objects.create(**THREAD)
        user = models.User.objects.create(**USER)
        thread.user = user
        thread.save()
        self.assertEqual(len(models.Thread.objects.filter(user=user.id)), 1)

    def test_user_message(self):
        thread = models.Thread.objects.create(**THREAD)
        thread.save()
        message = models.Message.objects.create(thread=thread, **MESSAGE)
        user = models.User.objects.create(**USER)
        message.user = user
        message.save()
        self.assertEqual(len(models.Message.objects.filter(user=user.id)), 1)


valid_tests = (
    (models.check_created, datetime(2007, 1, 1, 1, 1, 1, 1, tzinfo=timezone.utc)),
    # (models.check_modified, datetime(2007, 1, 1, 1, 1, 1, 1, tzinfo=timezone.utc)),
    # (models.check_positive, 1),
    # (models.check_year, 2007),
)
invalid_tests = (
    (models.check_created, datetime(3000, 1, 1, 1, 1, 1, 1, tzinfo=timezone.utc)),
    # (models.check_modified, datetime(3000, 1, 1, 1, 1, 1, 1, tzinfo=timezone.utc)),
    # (models.check_positive, -1),
    # (models.check_year, 3000),
)


def create_validation_test(validator, value, valid=True):
    def test(self):
        with self.assertRaises(ValidationError):
            validator(value)
    return lambda _: validator(value) if valid else test


invalid_methods = {
    f'test_invalid_{args[0].__name__}': create_validation_test(*args, False) for args in invalid_tests
}
valid_methods = {
    f'test_valid_{args[0].__name__}': create_validation_test(*args) for args in valid_tests
}
TestValidators = type('TestValidators', (TestCase,), invalid_methods | valid_methods)
