from django.contrib import admin
from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from .models import User, Section, Thread, Message, SectionThread
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin


admin.site.register(User, UserAdmin)


class SectionThreadInline(admin.TabularInline):
    model = SectionThread
    extra = 1
    

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