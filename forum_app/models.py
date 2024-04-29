from django.db import models
from uuid import uuid4
from datetime import datetime, date, timezone
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.conf.global_settings import AUTH_USER_MODEL


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


class User(UUIDMixin, CreatedMixin):
    login = models.TextField('login', null=False, blank=False, max_length=NAME_MAX_LENGTH)
    password = models.TextField('password', null=False, blank=False, max_length=NAME_MAX_LENGTH)
    mail = models.TextField('mail',  null=False, blank=False, max_length=MAIL_MAX_LEN)

    def __str__(self) -> str:
        return self.login
        
    class Meta:
        db_table = '"forum"."user"'
        ordering = ['login']
        verbose_name = 'user'
        verbose_name_plural = 'users'


class Thread(UUIDMixin, CreatedMixin):
    title = models.TextField('title', null=False, blank=False, max_length=TITLE_MAX_LEN)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = '"forum"."thread"'
        ordering = ['title']
        verbose_name = 'thread'
        verbose_name_plural = 'threads'


class Section(UUIDMixin):
    name = models.TextField('name', null=False, blank=False, max_length=NAME_MAX_LENGTH)
    threads = models.ManyToManyField(Thread, verbose_name='thread', through='SectionThread')

    class Meta:
        db_table = '"forum"."section"'
        ordering = ['name']
        verbose_name = 'section'
        verbose_name_plural = 'sections'


class SectionThread(UUIDMixin):
    section = models.ForeignKey(Section, verbose_name='section', on_delete=models.CASCADE)
    thread = models.ForeignKey(Thread, verbose_name='thraed', on_delete=models.CASCADE)

    class Meta:
        db_table = '"forum"."section_thread"'
        unique_together = (
            ('section', 'thread'),
        )
        verbose_name = 'relationship section thread'
        verbose_name_plural = 'relationships section thread'


class Message(UUIDMixin, CreatedMixin):
    message_body = models.TextField('message_body')
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = '"forum"."message"'
        ordering = ['created']
        verbose_name = 'message'
        verbose_name_plural = 'messages'