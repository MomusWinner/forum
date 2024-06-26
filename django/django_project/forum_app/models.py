"""Forums models."""
from datetime import datetime, timezone
from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from martor.models import MartorField

NAME_MAX_LENGTH = 100
TITLE_MAX_LEN = 100
DESCRIPTION_MAX_LEN = 4000
PASSWORD_MAX_LEN = 100
MAIL_MAX_LEN = 100


def get_datetime():
    return datetime.now(timezone.utc)


class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    class Meta:
        abstract = True


def check_created(dt: datetime):
    if dt > get_datetime():
        raise ValidationError(
            'Date and time is bigger than current!',
            params={'created': dt},
        )


class CreatedMixin(models.Model):
    created = models.DateTimeField(
        'created',
        null=True, blank=True,
        default=get_datetime,
        validators=[check_created],
    )

    class Meta:
        abstract = True


class User(UUIDMixin, AbstractUser):
    class Meta:
        db_table = 'user'
        ordering = ['last_name']
        verbose_name = 'user'
        verbose_name_plural = 'users'


class Thread(UUIDMixin, CreatedMixin):
    title = models.TextField('title', null=False, blank=False, max_length=TITLE_MAX_LEN)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    sections = models.ManyToManyField('Section', verbose_name='sections', through='SectionThread')

    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = 'thread'
        ordering = ['title']
        verbose_name = 'thread'
        verbose_name_plural = 'threads'


class Section(UUIDMixin):
    name = models.TextField(
        'name', null=False, blank=False, unique=True, max_length=NAME_MAX_LENGTH,
    )
    threads = models.ManyToManyField(Thread, verbose_name='threads', through='SectionThread')

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'section'
        ordering = ['name']
        verbose_name = 'section'
        verbose_name_plural = 'sections'


class SectionThread(UUIDMixin):
    section = models.ForeignKey(
        Section, null=True, blank=True, verbose_name='section', on_delete=models.CASCADE,
    )
    thread = models.ForeignKey(
        Thread, null=True, blank=True, verbose_name='thraed', on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return f'{self.section}: {self.thread}'

    class Meta:
        db_table = 'section_thread'
        unique_together = (
            ('section', 'thread'),
        )
        verbose_name = 'relationship section thread'
        verbose_name_plural = 'relationships section thread'


class Message(UUIDMixin, CreatedMixin):
    message_body = MartorField('message_body', null=False, max_length=DESCRIPTION_MAX_LEN)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return f'{self.message_body}'

    class Meta:
        db_table = 'message'
        ordering = ['created']
        verbose_name = 'message'
        verbose_name_plural = 'messages'
