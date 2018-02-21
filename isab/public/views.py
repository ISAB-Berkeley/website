# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import Event

def index(request):
    return render(request, 'public/index.html')

def about(request):
    return render(request, 'public/about.html')

def committees(request):
    return render(request, 'public/committees.html')

def events(request):
    all_events = Event.objects.all()
    context = {'all_events': all_events}
    return render(request, 'public/events.html', context)

def event(request, event_id):
    event = Event.objects.filter(id=event_id)[0]
    context = {'event': event}
    return render(request, 'public/event.html', context)

def contact(request):
    return render(request, 'public/contact.html')

def apply(request):
    return render(request, 'public/apply.html')
