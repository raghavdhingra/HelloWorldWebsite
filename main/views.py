from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
from django.contrib.auth.models import User,Group
from login.views import TeamUrlData, MemberDetails
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.template.loader import render_to_string
from .models import TeamMember
from login.views import *
import json
import requests

# Create your views here.
def home(request):
    username = ""
    teamMember = TeamMember.objects.all()
    if request.user.is_authenticated:
        print(str(request.user) + "\n")
        print(str(request.user.id) + "\n")
        username = User.objects.filter(pk=request.user.id)[0].first_name
        if username == '':
            username = request.user.username
    context = {
        "title":"Home | HelloWorld",
        "meta_title":"HelloWorld | HOME",
        "meta_description":"Welcome to the HelloWorld website. HelloWorld is the technical society of GTBIT. We aim to impart our knowledge and guidance to the young minds to create and improvise",
        "teamMembers": teamMember,
        "username": username,
        "developer":TeamMember.objects.filter(user_name='raghav')[0].profile_picture,
    }
    return render(request,'home.html',context)

def about(request):
    username = ""
    if request.user.is_authenticated:
        username = User.objects.filter(pk=request.user.id)[0].first_name
        if username == '':
            username = request.user.username
    context = {
        "title":"About | HelloWorld",
        "meta_title":"HelloWorld | ABOUT",
        "meta_description":"Since the establishment of our team, we have created a team of minds with a varied skill set. Know more about us!",
        "username": username,
        "developer":TeamMember.objects.filter(user_name='raghav')[0].profile_picture,
    }
    return render(request,'about.html',context)

def contact(request):
    username = ""
    messageStatus = ""
    if request.user.is_authenticated:
        username = User.objects.filter(pk=request.user.id)[0].first_name
        if username == '':
            username = request.user.username

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        query = request.POST.get('query')

        mail_context = {
            "first": name.split(' ')[0],
            "email":email,
            "name": name,
            "phone":phone,
            "query": query,
        }
        html_content = render_to_string('email.html',mail_context)
        info_to_send = str(name) + "\n" + str(email) + "\n" + str(query)
        msg = EmailMultiAlternatives("{}'s Query ".format(name), info_to_send, 'contact@helloworldofficial.in', ['info@helloworldofficial.in',email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        messageStatus = "200"

    context = {
        "title":"Contact | HelloWorld",
        "meta_title":"HelloWorld | GTBIT",
        "meta_description":"This is the official website of HELLOWORLD",
        "username": username,
        "developer":TeamMember.objects.filter(user_name='raghav')[0].profile_picture,
        "messageStatus": messageStatus,
    }
    return render(request,'contact.html',context)

def team(request):
    username = ""
    if request.user.is_authenticated:
        username = User.objects.filter(pk=request.user.id)[0].first_name
        if username == '':
            username = request.user.username

    teamMember = TeamMember.objects.all()

    context = {
        "title":"Team | HelloWorld",
        "meta_title":"HelloWorld | Know Our Team",
        "meta_description":"Since the establishment of our team, we have created a team of minds with a varied skill set. We work in various fields to develop and implement. We aren't just a team but a family sharing bonds and knowledge with a common aim to serve the era of globalisation and digitalization. Want to know more about our journey and plans ahead?",
        "username": username,
        "developer":TeamMember.objects.filter(user_name='raghav')[0].profile_picture,
        "teamMember": teamMember,
    }
    return render(request,'team.html',context)


def event(request):
    username = ""
    if request.user.is_authenticated:
        username = User.objects.filter(pk=request.user.id)[0].first_name
        if username == '':
            username = request.user.username
    context = {
        "title":"Events | HelloWorld",
        "meta_title":"HelloWorld | GTBIT",
        "meta_description":"Participate in our offline and online events to test your skills, keep the competitive spirits high and not to forget the goodies!  Login now to know more.",
        "username": username,
        "developer":TeamMember.objects.filter(user_name='raghav')[0].profile_picture,
    }
    return render(request,'event.html',context)


def profile(request):
    username = ""
    if request.user.is_authenticated:
        username = User.objects.filter(pk=request.user.id)[0].first_name
        user_data = TeamMember.objects.filter(user=request.user)[0]
        user_image_url = user_data.profile_picture
        interest_arr = user_data.specialisation.split('|')

        if interest_arr[0] == "":
            interest_arr[0] = "No Particular Interest"

        if username == '':
            username = request.user.username
    try:
        context = {
            "username":username,
        "developer":TeamMember.objects.filter(user_name='raghav')[0].profile_picture,
            "header": "Your Profile",
            "title": str(username) + " | Profile",
            "meta_title":"HelloWorld | GTBIT",
            "meta_description":"This is the official website of HELLOWORLD",
            "contact": user_data.contact,
            "profilePic": user_image_url,
            "interest": interest_arr[0],
            "birth": user_data.birth_date,
            "description":user_data.description,
            "designation":user_data.designation,
            "skills": user_data.skills['skill'],
            "links": user_data.links,
            "passing_year": user_data.passing_year,
            "degree": user_data.degree,
            "college": user_data.college,
        }
    except:
        return HttpResponse("<center><h1>Access Denied</h1><h3>You are not allowed to access this tab</h3><h4>Only authorised user can have access to this page.</h4><h3>Go Back</h3></center>")
    return render(request,'profile.html',context)

def edit(request):
    print(str(request.user) + "\n")
    print(str(request.user.id) + "\n")
    username = ""
    if request.user.is_authenticated:
        user_data = TeamMember.objects.filter(user=request.user)[0]
        user_image_url = user_data.profile_picture
        interest_arr = user_data.specialisation.split('|')

        skill_data = ""
        skill_arr = user_data.skills['skill']
        for obj in skill_arr:
            if skill_data == "":
                skill_data = skill_data + str(obj)
            else:
                skill_data = skill_data + "," + str(obj)

        username = User.objects.filter(pk=request.user.id)[0].first_name

        if username == '':
            username = request.user.username

    if request.method == 'POST':
        username = request.user.username
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        college = request.POST.get('college')
        degree = request.POST.get('degree')
        passing_year = request.POST.get('pass_year')
        birth = request.POST.get('birth')
        interest = request.POST.get('interest')
        skill = request.POST.get('skill')
        skill_list = str(skill).split(',')
        
        teamSkill = {
            'skill':skill_list,
        }
        
        if interest == 'OTHER - Specify|17':
            interest = request.POST.get('otherInterest') + "|17"


        designation = request.POST.get('designation')
        description = request.POST.get('description')
        links = { 
            'facebook': request.POST.get('facebook'),
            'twitter': request.POST.get('twitter'),
            'github': request.POST.get('github'),
        }
        contact = {  
            'email': request.user.email,
            'phone': request.POST.get('phone'),
            'address': ""
        }

        User.objects.filter(pk=request.user.id).update(first_name = first_name, last_name = last_name)
        TeamMember.objects.filter(pk=request.user.id).update(
            first_name = first_name,
            last_name = last_name,
            user_name = request.user.username,
            specialisation = interest,
            birth_date = birth,
            description = description,
            designation = designation,
            college = college,
            degree = degree,
            passing_year = passing_year,
            links = links,
            skills = teamSkill,
            contact = contact,
            )

        # if request.FILES['profile_pic']:
        #     profile_pic = request.FILES['profile_pic']
        #     user_data.profile_picture = profile_pic

        return redirect('/user/profile')
    try:
        context = {
            "username":username,
            "header": "Edit Your Profile",
            "developer":TeamMember.objects.filter(user_name='raghav')[0].profile_picture,
            "title": str(username) + " | Edit",
            "meta_title":"HelloWorld | GTBIT",
            "meta_description":"This is the official website of HELLOWORLD",
            "contact": user_data.contact,
            "email": User.objects.filter(pk=request.user.id)[0].email,
            "profilePic": user_image_url,
            "interest": user_data.specialisation,
            "otherInterest": interest_arr[0],
            "birth": str(user_data.birth_date),
            "description":user_data.description,
            "designation":user_data.designation,
            "skills": skill_data,
            "links": user_data.links,
            "passing_year": user_data.passing_year,
            "degree": user_data.degree,
            "college": user_data.college,
        }
    except:
        return HttpResponse("<center><h1>Access Denied</h1><h3>You are not allowed to access this tab</h3><h4>Only authorised user can have access to this page.</h4><h3>Go Back</h3></center>")
    try:
        context['selectedIndex'] = interest_arr[1]
    except:
        context['selectIndex']= 0
    return render(request,'edit.html',context)

def changepassword(request):
    username = ""
    err = ""
    if request.user.is_authenticated:
        username = User.objects.filter(pk=request.user.id)[0].first_name
        if username == '':
            username = request.user.username
    context = {
        "username":username,
        "header": "Change Your Password",
        "title": str(username) + " | Change Password",
        "meta_title":"HelloWorld | GTBIT",
        "meta_description":"This is the official website of HELLOWORLD",
        "err":err,
        "developer":TeamMember.objects.filter(user_name='raghav')[0].profile_picture,
    }
    return render(request,'changepassword.html',context)

def resume(request):
    username = ""
    err = ""
    if request.user.is_authenticated:
        username = User.objects.filter(pk=request.user.id)[0].first_name
        if username == '':
            username = request.user.username
    context = {
        "username":username,
        "header": "Build Your Resume",
        "title": str(username) + " | Build Resume",
        "meta_title":"HelloWorld | GTBIT",
        "meta_description":"This is the official website of HELLOWORLD",
        "err":err,
        "developer":TeamMember.objects.filter(user_name='raghav')[0].profile_picture,
    }
    return render(request,'resume.html',context)

def uploadFile(file):
    cloudinary.uploader.upload(file)

def verifyIt(request):
    return render(request,'../.well-known/acme-challenge/LoKO_jQCYTp5Sm7Vrj6sUtkqQ89khvJg0KRhWHZquoM')

def footerForm(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        query = request.POST.get('message')
        
        mail_context = {
            "first": name.split(' ')[0],
            "email":email,
            "name": name,
            "query": query,
        }
        html_content = render_to_string('email.html',mail_context)
        info_to_send = str(name) + "\n" + str(email) + "\n" + str(query)
        msg = EmailMultiAlternatives("{}'s Query ".format(name), info_to_send, 'contact@helloworldofficial.in', ['info@helloworldofficial.in',email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

    return redirect('/')