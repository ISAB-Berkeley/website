from django.urls import path
from django.conf.urls import handler404

from . import views

urlpatterns = [
    path('about', views.about, name='about'),
    path('committees', views.committees, name='committees'),
    path('events', views.events, name='events'),
    path('events/<int:event_id>', views.event, name='event'),
    path('contact', views.contact, name='contact'),
    path('apply', views.apply, name='apply'),
    path('', views.index, name='index'),
]

handler404 = views.handler404
