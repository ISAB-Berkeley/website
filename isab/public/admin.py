# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Event
from .models import EventImage
from .models import Semester

class EventImageInline(admin.TabularInline):
    model = EventImage
    extra = 20

class EventAdmin(admin.ModelAdmin):
    inlines = [EventImageInline,]

admin.site.register(Event, EventAdmin)
admin.site.register(Semester)