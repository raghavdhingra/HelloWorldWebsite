from django.db import models
from django.conf import settings
import json
from django.utils import timezone
# from jsonfield import JSONField
from django.contrib.postgres.fields import JSONField , ArrayField ,DateTimeRangeField
from .json import *



# Create your models here.
class TeamMember(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 200, blank=True, null=False,default='')
    last_name = models.CharField(max_length = 200, blank=True, null=False,default='')
    # phone_number = models.CharField(blank=True, null=False,default='',max_length=10)
    profile_picture = models.ImageField(blank=True, null=False)
    authorised = models.BooleanField(blank=False,null=False,default=False)
    specialisation = models.CharField(max_length=100,blank=True,null=False,default='')
    birth_date = models.DateField(blank=True, null=False,default=timezone.now)
    # email = models.EmailField(blank=True, null=False,default='')
    joined_on = models.DateTimeField(blank=True, null=False,default=timezone.now)
    description = models.TextField(blank=True,null=False,default='')
    designation = models.CharField(blank=True,null=False,max_length=100,default='Core Member')
    # facebook_link = models.CharField(max_length=200, blank=True,null=False,default='https://www.facebook.com/')
    # twitter_link = models.CharField(max_length=200, blank=True,null=False,default='https://twitter.com')
    # github_link = models.CharField(max_length=200, blank=True,null=False,default='https://github.com/')

    skills = models.TextField(blank=True,null=False,default=json.dumps(skills))
    education = models.TextField(blank=True,null=False,default=json.dumps(education))
    links = models.TextField(blank=True,null=False,default=json.dumps(links))
    contact = models.TextField(blank=True,null=False,default=json.dumps(contact))

    def publish(self):
        self.joined_on = timezone.now()
        self.save()

    def __str__(self):
        return self.first_name