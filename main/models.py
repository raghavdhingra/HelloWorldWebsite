from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils import timezone
from django.contrib.postgres.fields import JSONField , ArrayField ,DateTimeRangeField
from .json import *



# Create your models here.
class TeamMember(models.Model):
    user = models.OneToOneField(User,primary_key=True,on_delete=models.CASCADE)
    user_name = models.CharField(max_length=200,blank=True,null=True,default='UserName')
    first_name = models.CharField(max_length = 200, blank=True, null=True,default='')
    last_name = models.CharField(max_length = 200, blank=True, null=True,default='')
    profile_picture = models.CharField(max_length = 300, blank=True, null=True,default='')
    authorised = models.BooleanField(blank=True,null=True,default=True)
    specialisation = models.CharField(max_length=100,blank=True,null=True,default='')
    birth_date = models.DateField(blank=True, null=True,default=timezone.now)
    joined_on = models.DateTimeField(blank=True, null=True,default=timezone.now)
    description = models.TextField(blank=True,null=True,default='')
    designation = models.CharField(blank=True,null=True,max_length=100,default='Member')
    skills = JSONField(default=skills)
    college = models.TextField(blank=True,null=True,default='')
    degree = models.TextField(blank=True,null=True,default='')
    passing_year = models.IntegerField(blank=True,null=True,default=2000)
    links = JSONField(default=links)
    contact = JSONField(default=contact)

    def publish(self):
        self.joined_on = timezone.now()
        self.save()

    def __str__(self):
        return self.user_name

class Events(models.Model):
    name = models.CharField(max_length = 200, blank=True, null=True,default='')
    event_pic = models.CharField(max_length = 400, blank=True, null=True,default='')
    date = models.DateField(blank=True, null=True,default=timezone.now)
    time = models.TimeField(blank=True, null=True,default=timezone.now)
    location = models.CharField(max_length = 300, blank=True, null=True,default='')
    location_link = models.CharField(max_length = 400, blank=True, null=True,default='')
    description = models.TextField(blank=True,null=True,default='')
    registration_link = models.CharField(max_length = 400, blank=True, null=True,default='')
    upcoming = models.BooleanField(blank=True,null=True,default=True)

    def publish(self):
        self.time = timezone.now()
        self.save()

    def __str__(self):
        return self.name

class Email(models.Model):
    name = models.CharField(max_length = 200, blank=True, null=True,default='raghav')
    email = ArrayField(models.CharField(max_length=300),default=email,null=True,blank=True)
    time = models.TimeField(blank=True, null=True,default=timezone.now)

    def publish(self):
        self.time = timezone.now()
        self.save()

    def __str__(self):
        return self.name
    
class Hackgtbit(models.Model):
    name = models.CharField(max_length = 200, blank=True, null=True,default='raghav')
    description = models.TextField(blank=True,null=True,default='')
    time = models.TimeField(blank=True, null=True,default="12:00:00")
    date = models.DateField(blank=True, null=True,default="2020-01-18")
    serial = models.CharField(max_length = 200, blank=True, null=True,default='')

    def __str__(self):
        return self.name
    