from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
from django.contrib.auth.models import User,Group
from login.views import TeamUrlData, MemberDetails
from .models import TeamMember
from login.views import *
import json
import requests

# Create your views here.
def home(request):
    username = ""
    teamMember = range(0,10)
    if request.user.is_authenticated:
        data = MemberDetails(request.user.id)
        username = data[0]['first_name']
        if username == '':
            username = request.user.username
    context = {
        "title":"Home | Hello World",
        "meta_title":"Hello World | GTBIT",
        "meta_description":"This is the official website of HELLO WORLD",
        "teamMembers": teamMember,
        "username": username,
    }
    return render(request,'home.html',context)

def about(request):
    username = ""
    if request.user.is_authenticated:
        data = MemberDetails(request.user.id)
        username = data[0]['first_name']
        if username == '':
            username = request.user.username
    context = {
        "title":"About | Hello World",
        "meta_title":"Hello World | GTBIT",
        "meta_description":"This is the official website of HELLO WORLD",
        "username": username,
    }
    return render(request,'about.html',context)

def contact(request):
    username = ""
    if request.user.is_authenticated:
        data = MemberDetails(request.user.id)
        username = data[0]['first_name']
        if username == '':
            username = request.user.username
    context = {
        "title":"Contact | Hello World",
        "meta_title":"Hello World | GTBIT",
        "meta_description":"This is the official website of HELLO WORLD",
        "username": username,
    }
    return render(request,'contact.html',context)

def team(request):
    username = ""
    if request.user.is_authenticated:
        data = MemberDetails(request.user.id)
        username = data[0]['first_name']
        if username == '':
            username = request.user.username
        check_auth = TeamMember.objects.filter(user_name = request.user)[0].first_name
        print(check_auth)
    # team = TeamUrlData()
    # print(team)
    context = {
        "title":"Team | Hello World",
        "meta_title":"Hello World | GTBIT",
        "meta_description":"This is the official website of HELLO WORLD",
        "username": username,
    }
    return render(request,'team.html',context)


def event(request):
    username = ""
    if request.user.is_authenticated:
        data = MemberDetails(request.user.id)
        username = data[0]['first_name']
        if username == '':
            username = request.user.username
    context = {
        "title":"Events | Hello World",
        "meta_title":"Hello World | GTBIT",
        "meta_description":"This is the official website of HELLO WORLD",
        "username": username,
    }
    return render(request,'event.html',context)


def profile(request):
    user_data = TeamMember.objects.filter(user=request.user)[0]
    # print(user_data)

    username = ""
    if request.user.is_authenticated:
        data = MemberDetails(request.user.id)
        username = data[0]['first_name']
        if username == '':
            username = request.user.username
    # print(user_data.birth_date)
    context = {
        "username":username,
        "header": "Your Profile",
        "title": str(username) + " | Profile",
        "meta_title":"Hello World | GTBIT",
        "meta_description":"This is the official website of HELLO WORLD",
        "name": str(user_data.first_name) + " " + str(user_data.last_name),
        "contact": user_data.contact,
        "profilePic": user_data.profile_picture,
        "interest": user_data.specialisation,
        "birth": user_data.birth_date,
        "description":user_data.description,
        "designation":user_data.designation,
        "skills": user_data.skills['skill'],
        "links": user_data.links,
    }
    return render(request,'profile.html',context)

def edit(request):
    username = ""
    if request.user.is_authenticated:
        data = MemberDetails(request.user.id)
        username = data[0]['first_name']
        if username == '':
            username = request.user.username
    context = {
        "username":username,
        "header": "Edit Your Profile",
        "title": str(username) + " | Edit",
        "meta_title":"Hello World | GTBIT",
        "meta_description":"This is the official website of HELLO WORLD",
    }
    return render(request,'edit.html',context)

def changepassword(request):
    username = ""
    err = ""
    if request.user.is_authenticated:
        data = MemberDetails(request.user.id)
        username = data[0]['first_name']
        if username == '':
            username = request.user.username
    context = {
        "username":username,
        "header": "Change Your Password",
        "title": str(username) + " | Change Password",
        "meta_title":"Hello World | GTBIT",
        "meta_description":"This is the official website of HELLO WORLD",
        "err":err,
    }
    return render(request,'changepassword.html',context)

def resume(request):
    username = ""
    err = ""
    if request.user.is_authenticated:
        data = MemberDetails(request.user.id)
        username = data[0]['first_name']
        if username == '':
            username = request.user.username
    context = {
        "username":username,
        "header": "Build Your Resume",
        "title": str(username) + " | Build Resume",
        "meta_title":"Hello World | GTBIT",
        "meta_description":"This is the official website of HELLO WORLD",
        "err":err,
    }
    return render(request,'resume.html',context)