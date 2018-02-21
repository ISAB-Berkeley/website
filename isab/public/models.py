# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from datetime import date

class Semester(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    location = models.TextField()
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    facebook = models.URLField()
    photo = models.FileField(upload_to="events")

    def __str__(self):
        return self.name
