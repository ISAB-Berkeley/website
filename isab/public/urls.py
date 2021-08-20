from django.urls import path

from . import views

urlpatterns = [
    path('about', views.about, name='about'),
    path('committees', views.committees, name='committees'),
    path('events', views.events, name='events'),
    path('events/<int:event_id>', views.event, name='event'),
    path('contact', views.contact, name='contact'),
    path('apply', views.apply, name='apply'),
    path('qanda', views.qanda, name='qanda'),
    path('news', views.news, name='news'),
    path('', views.index, name='index'),
]