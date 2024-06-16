"""Admin."""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db import models
from martor.widgets import AdminMartorWidget

from .models import Message, Section, SectionThread, Thread, User

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
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }
