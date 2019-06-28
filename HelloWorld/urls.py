"""HelloWorld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
import main.views

urlpatterns = [
    path('admin', admin.site.urls,name="admin"),
    path('',main.views.home,name="home"),
    path('about',main.views.about,name="about"),
    path('contact',main.views.contact,name="contact"),
    path('know-our-team',main.views.team,name="team"),
    path('upcoming-events',main.views.event,name="event"),
]
