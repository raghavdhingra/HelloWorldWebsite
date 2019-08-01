"""helloworld URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from main import views as mainView
from login import views as loginView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin', admin.site.urls,name="admin"),
    path('', mainView.home,name="home"),
    path('about', mainView.about,name="about"),
    path('contact', mainView.contact,name="contact"),
    path('know-our-team', mainView.team,name="team"),
    path('upcoming-and-past-events', mainView.event,name="event"),
    path('teamapi', mainView.MemberList.as_view()),
    path('teamapi/id=<int:UserId>', mainView.SingleMember.get),
    path('testurl',mainView.testUrl, name="testUrl"),
    path('authorization',loginView.auth, name="auth")
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)