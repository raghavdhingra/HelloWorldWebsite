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
    user_name = models.CharField(max_length=200,blank=True,null=False,default='UserName')
    first_name = models.CharField(max_length = 200, blank=True, null=False,default='')
    last_name = models.CharField(max_length = 200, blank=True, null=False,default='')
    profile_picture = models.ImageField(blank=True, null=False)
    authorised = models.BooleanField(blank=False,null=False,default=False)
    specialisation = models.CharField(max_length=100,blank=True,null=False,default='')
    birth_date = models.DateField(blank=True, null=False,default=timezone.now)
    joined_on = models.DateTimeField(blank=True, null=False,default=timezone.now)
    description = models.TextField(blank=True,null=False,default='')
    designation = models.CharField(blank=True,null=False,max_length=100,default='Core Member')
    skills = JSONField(default=skills)
    education = JSONField(default=education)
    links = JSONField(default=links)
    contact = JSONField(default=contact)

    def publish(self):
        self.joined_on = timezone.now()
        self.save()

    def __str__(self):
        return self.first_name