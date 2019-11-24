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
from django.views.static import serve
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

from django.conf.urls import handler404, handler500

sitemaps = {
    'static': StaticViewSitemap,
}

teampi = 'teamapi/key=1a35d89ise039'
eventapi = 'eventapi/key=1a35d89ise039'

urlpatterns = [
    path('admin', admin.site.urls,name="admin"),
    path('', mainView.home,name="home"),
    path('add-email',mainView.addEmailId,name="addEmailId"),
    path('about', mainView.about,name="about"),
    path('contact', mainView.contact,name="contact"),
    path('gallery', mainView.gallery,name="gallery"),
    path('know-our-team', mainView.team,name="team"),
    path('upcoming-and-past-events', mainView.event,name="event"),
    path('hack-gtbit-2.0', mainView.hackgtbit,name="hackgtbit"),

    path('code-of-conduct', mainView.code_of_conduct,name="conduct"),
    path('terms-and-condition', mainView.terms_and_cond,name="terms"),
    path('privacy-policy', mainView.privacy_policy,name="privacy"),
    path('frequently-ask-questions', mainView.faqs,name="faq"),

    path(teampi, mainView.MemberList.as_view()),
    path(eventapi, mainView.EventList.as_view()),
    path('mailing-list',mainView.MailingList.as_view()),
    path('teamapi/id=<int:UserId>', mainView.SingleMember.get),
    path('authorization',loginView.auth, name="auth"),
    path('logout',loginView.log_out, name="logout"),
    path('login',loginView.log_in, name="login"),
    path('signup',loginView.sign_up, name="signin"),
    path('user/profile',mainView.profile,name='profile'),
    path('user/edit',mainView.edit,name='edit'),
    path('user/change-password',mainView.changepassword,name='changepassword'),
    path('user/build-your-resume',mainView.resume,name='resume'),

    path('user/uploadImage',mainView.uploadImage,name='uploadImage'),

    path('user/manage-event',mainView.manageevent,name="manageevent"),
    path('user/manage-event/add-event',mainView.addevent,name="addEvent"),
    path('user/manage-event/delete-event',mainView.deleteevent,name="deleteEvent"),
    path('user/manage-event/event=<slug>',mainView.post_by_event,name="post_by_event"),
    path('user/manage-event/single-event',mainView.single_event,name="singleEvent"),
    path('user/manage-event/saveSingleEvent',mainView.saveSingleEvent,name="saveSingleEvent"),
    path('user/manage-event/saveSingleEventImage',mainView.saveSingleEventImage,name="saveSingleEventImage"),

    path('user/manage-team',mainView.manageteam,name="manageteam"),
    path('user/manage-team/user=<slug>',mainView.post_by_username,name="post_by_username"),
    path('user/manage-team/single-member',mainView.single_member,name="singleMember"),
    path('user/manage-team/saveSingle',mainView.saveSingle,name="saveSingle"),

    path('query',mainView.footerForm,name="footerForm"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps }, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', TemplateView.as_view(template_name="./robots.txt", content_type='text/plain')),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT, 'show_indexes': settings.DEBUG})
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = mainView.error_404
handler500 = mainView.error_500