from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
from django.contrib.auth.models import User,Group
from .models import TeamMember
from login.views import *
import json
import requests

# Create your views here.
def home(request):
    teamMember = range(0,10)
    context = {
        "title":"Home | Hello World",
        "meta_title":"Hello World | GTBIT",
        "meta_description":"This is the official website of HELLO WORLD",
        "teamMembers": teamMember
    }
    return render(request,'home.html',context)

def about(request):
    context = {
        "title":"About | Hello World",
        "meta_title":"Hello World | GTBIT",
        "meta_description":"This is the official website of HELLO WORLD"
    }
    return render(request,'about.html',context)

def contact(request):
    context = {
        "title":"Contact | Hello World",
        "meta_title":"Hello World | GTBIT",
        "meta_description":"This is the official website of HELLO WORLD"
    }
    return render(request,'contact.html',context)

def team(request):
    team = TeamUrlData()
    y = team[0]['contact']
    # x = json.loads(y.text)
    x = json.loads(y)
    print(x['phone'])
    context = {
        "title":"Team | Hello World",
        "meta_title":"Hello World | GTBIT",
        "meta_description":"This is the official website of HELLO WORLD"
    }
    return render(request,'team.html',context)


def event(request):
    context = {
        "title":"Events | Hello World",
        "meta_title":"Hello World | GTBIT",
        "meta_description":"This is the official website of HELLO WORLD"
    }
    return render(request,'event.html',context)

def post(request):
    return HttpResponse()
