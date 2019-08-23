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
from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from helloworld.settings import *
from main import views as mainView
from login import views as loginView
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import views
from .sitemap import *

sitemaps = {
    'static': StaticViewSitemap,
}

teampi = 'teamapi/key=1a35d89ise039'

urlpatterns = [
    path('admin', admin.site.urls,name="admin"),
    path('', mainView.home,name="home"),
    path('about', mainView.about,name="about"),
    path('contact', mainView.contact,name="contact"),
    path('know-our-team', mainView.team,name="team"),
    path('upcoming-and-past-events', mainView.event,name="event"),
    path(teampi, mainView.MemberList.as_view()),
    path('teamapi/id=<int:UserId>', mainView.SingleMember.get),
    path('testurl',mainView.testUrl, name="testUrl"),
    path('authorization',loginView.auth, name="auth"),
    path('logout',loginView.log_out, name="logout"),
    path('login',loginView.log_in, name="login"),
    path('signup',loginView.sign_up, name="signin"),
    path('user/profile',mainView.profile,name='profile'),
    path('user/edit',mainView.edit,name='edit'),
    path('user/change-password',mainView.changepassword,name='changepassword'),
    path('user/build-your-resume',mainView.resume,name='resume'),
    path('query',mainView.footerForm,name="footerForm"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps }, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', TemplateView.as_view(template_name="./robots.txt", content_type='text/plain')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(MEDIA_URL,document_root=MEDIA_ROOT)