# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from datetime import date

def event_folder(event, filename):
    return '/'.join(['events', event.semester.code, event.name.lower(), filename])

class Semester(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    @property
    def short(self):
        return self.name[:2] + " '" + self.name.split(" ", 1)[1][2:]
    
    @property
    def code(self):
        return self.name.lower().replace(" ", "_")

class Event(models.Model):
    def image_folder(instance, filename):
        return event_folder(instance, filename)

    name = models.CharField(max_length=30)
    description = models.TextField()
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    location = models.TextField()
    cover = models.ImageField(upload_to=image_folder)

    def __str__(self):
        return self.name

    @property
    def short(self):
        return self.description.replace("!", ".").split(".", 1)[0] + "!"

class EventImage(models.Model):
    def image_folder(instance, filename):
        return event_folder(instance.event, filename)
    
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=image_folder)
