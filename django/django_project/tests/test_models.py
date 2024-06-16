"""Models test."""
from datetime import datetime, timezone
from types import MappingProxyType

from django.core.exceptions import ValidationError
from django.test import TestCase

from forum_app import models

THREAD = MappingProxyType({'title': 'test_thread'})
SECTION = MappingProxyType({'name': 'test_section'})
USER = MappingProxyType({'username': 'test_username', 'password': 'test_Password112233'})
MESSAGE = MappingProxyType({'message_body': 'some message'})


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
)

invalid_tests = (
    (models.check_created, datetime(3000, 1, 1, 1, 1, 1, 1, tzinfo=timezone.utc)),
)


def create_validation_test(validator, validator_args, valid=True):
    def test(self):
        with self.assertRaises(ValidationError):
            validator(validator_args)
    return lambda _: validator(validator_args) if valid else test


invalid_methods = {
    f'test_invalid_{args[0].__name__}':
    create_validation_test(*args, valid=False) for args in invalid_tests
}
valid_methods = {
    f'test_valid_{args[0].__name__}':
    create_validation_test(*args) for args in valid_tests
}

TestValidators = type('TestValidators', (TestCase,), invalid_methods | valid_methods)
