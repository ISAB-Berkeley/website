# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from datetime import date

class Event(models.Model):
    event_name = models.CharField(max_length=30)
    description = models.TextField()
    location = models.TextField()
    semester = models.TextField(default="") # Options
    facebook_link = models.URLField()
    picture_link = models.URLField()
    photo_file = models.FileField(upload_to="events_imgs")

    def __str__(self):
        return self.event_name
