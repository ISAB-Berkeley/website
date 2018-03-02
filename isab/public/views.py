# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import EmailMessage
from .models import Event, Semester
from .forms import ContactForm

def index(request):
    return render(request, 'public/index.html')

def about(request):
    return render(request, 'public/about.html')

def committees(request):
    return render(request, 'public/committees.html')

def events(request):
    semesters = Semester.objects.all()
    events = Event.objects.all()
    context = {'events': events, 'semesters': semesters}
    return render(request, 'public/events.html', context)

def event(request, event_id):
    event = Event.objects.filter(id=event_id)[0]
    images = event.images.all()
    context = {'event': event, 'images': images}
    return render(request, 'public/event.html', context)

def contact(request):
    success = False
    errors = []
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            msg = "FROM: " + form.cleaned_data.get('email')
            msg += "\n\n"
            msg += form.cleaned_data.get('comment')
            head = form.cleaned_data.get('subject')
            if len(head) < 1:
                head = "No Subject"
            email = EmailMessage(
                head,
                msg,
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_CONTACT_TARGET],
                reply_to=[form.cleaned_data.get('email')]
            )
            count = email.send(fail_silently=True)
            if count < 1:
                errors.append("Could not send your message at this time.")
            else:
                success = True
                form = ContactForm()
        else:
            for field in form:
                for error in field.errors:
                    errors.append(error)
    else:
        form = ContactForm()
    context = {'form': form, 'errors': errors, 'success': success}
    return render(request, 'public/contact.html', context)

def apply(request):
    return render(request, 'public/apply.html')
