# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Event
from .models import Semester

admin.site.register(Event)
admin.site.register(Semester)