from django.contrib import admin
from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from .models import User, Section, Thread, Message, SectionThread
from django.utils.translation import gettext_lazy as _

class SectionThreadInline(admin.TabularInline):
    model = SectionThread
    extra = 1


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    model = Section
    inlines = (SectionThreadInline,)


@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    model = Thread
    inlines = (SectionThreadInline,)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    model = Message