from typing import Any
from django.db import models
from uuid import uuid4
from datetime import datetime, date, timezone
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django_ckeditor_5.fields import CKEditor5Field

NAME_MAX_LENGTH = 100
TITLE_MAX_LEN = 100
DESCRIPTION_MAX_LEN = 1000
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
            _('Date and time is bigger than current!'),
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
        db_table = '"forum"."user"'
        ordering = ['last_name']
        verbose_name = 'user'
        verbose_name_plural = 'users'


class Thread(UUIDMixin, CreatedMixin):
    title = models.TextField('title', null=False, blank=False, max_length=TITLE_MAX_LEN)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    sections = models.ManyToManyField("Section", verbose_name='sections', through='SectionThread')

    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = '"forum"."thread"'
        ordering = ['title']
        verbose_name = 'thread'
        verbose_name_plural = 'threads'


class Section(UUIDMixin):
    name = models.TextField('name', null=False, blank=False, max_length=NAME_MAX_LENGTH)
    threads = models.ManyToManyField(Thread, verbose_name='threads', through='SectionThread')

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = '"forum"."section"'
        ordering = ['name']
        verbose_name = 'section'
        verbose_name_plural = 'sections'


class SectionThread(UUIDMixin):
    section = models.ForeignKey(Section, verbose_name='section', on_delete=models.CASCADE)
    thread = models.ForeignKey(Thread, verbose_name='thraed', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.section}: {self.thread}'

    class Meta:
        db_table = '"forum"."section_thread"'
        unique_together = (
            ('section', 'thread'),
        )
        verbose_name = 'relationship section thread'
        verbose_name_plural = 'relationships section thread'


class Message(UUIDMixin, CreatedMixin):
    message_body = CKEditor5Field('message_body', max_length=2000, config_name='extends')
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)


    def __str__(self) -> str:
        return f'{self.message_body}'

    class Meta:
        db_table = '"forum"."message"'
        ordering = ['created']
        verbose_name = 'message'
        verbose_name_plural = 'messages'