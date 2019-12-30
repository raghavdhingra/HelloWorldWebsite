#Imports statement
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from main.serializer import *
from rest_framework import status
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
import json
import requests
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User,Group
from main.models import *
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

#Handling Messages
#
#For Login Requests
#  --> request.session['msg']='core'
#  --> request.session['msg']='not_core'
#  --> request.session['msg']='notFound'
#  --> request.session['msg']='pass_not_match'


# Create your views here.
def TeamUrlData():
    try:
        data = requests.get('https://hello-world15.herokuapp.com/teamapi')
        resp = json.loads(data.text)
        print("\n\n Data is Fetch From Main API\n")
    except:
        data = requests.get('https://127.0.0.1:8000/teamapi')    
        resp = json.loads(data.text)
        print("\n\n Data is Fetched from Local API \n\n")
    return resp

def MemberDetails(userId):
    try:
        url = "https://hello-world15.herokuapp.com/teamapi/id=" + str(userId)
        data = requests.get(url)
        resp = json.loads(data.text)
    except:
        url = "https://127.0.0.1:8000/teamapi/id=" + str(userId)
        data = requests.get(url)
        resp = json.loads(data.text)
    return resp

#APIs
class MemberList(APIView):
    def get(self,request):
        member = TeamMember.objects.all()
        serializer = MemberSerialiser(member, many=True)
        return JsonResponse(serializer.data,safe=False)
    def post(self):
        pass

class EventList(APIView):
    def get(self,request):
        member = Events.objects.all()
        serializer = EventSerialiser(member, many=True)
        return JsonResponse(serializer.data,safe=False)
    def post(self):
        pass

class MailingList(APIView):
    def get(self,request):
        member = Email.objects.filter(name='raghav')
        serializer = MailSerialiser(member, many=True)
        return JsonResponse(serializer.data,safe=False)
    def post(self):
        pass

class SingleMember(APIView):
    def get(self,UserId):
        member = TeamMember.objects.filter(pk = UserId)
        serializer = MemberSerialiser(member, many=True)
        return JsonResponse(serializer.data,safe=False)
    def post(self):
        pass

# Classes Ends


#Functions are defined here

def auth(request):
    username = ""
    if request.user.is_authenticated:
        username = User.objects.filter(pk=request.user.id)[0].first_name
        if username == '':
            username = request.user.username
    context = {
        "title":"Authorization",
        "meta_title":"LogIn/SignUp - HelloWorld",
        "meta_description":"Sign-up / Login to the HelloWorld website to stay updated of what's next on the events timeline. Moreover login to contact our team for doubts and support.",
        "username": username,
    }
    return render(request,'auth.html',context)


def log_out(request):
    try:
        logout(request)
        return redirect('/')
    except Exception as e:
        print("\n\n An Error Occured: " + str(e) + "\n\n")
        return HttpResponse("Something Went Wrong...")

def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        core = request.POST.get('coremember')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            request.session['msg']=''
            if core == 'on':
                check_auth = TeamMember.objects.filter(user_name=username)[0].authorised
                if check_auth == True:
                    request.session['message']='core'                
                elif check_auth == False:
                    print('\n You are not a Core Member \n')
                    request.session['msg']='not_core'
                else:
                    return HttpResponse("<h1>Some Error Occured While Processing Your Request...</h2>")
            login(request,user)
            print("\n Logged In successfully as: " + str(username) + "\n")
            return redirect('/')
        else:
            request.session['msg']='notFound'
            return redirect('/authorization')        
    else:
        print("\n Successfully Logged-In as" + str(request.user.username) + "\n")
        return redirect("<h1>Some Error Has Been Occured...</h1>")

def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('sign_username')
        password = request.POST.get('sign_password')
        confpass = request.POST.get('confirmPassword')
        email = request.POST.get('sign_email')
        if confpass == password:
            new_user = User.objects.create_user(username = username, email = email, password = password)
            new_user.save()
            print("\n" + 'New Account has been created with username :' + str(username) + "\n")
            user = authenticate(username = username, password = password)
            login(request,user)
            print("\n" + 'successfully Logined as ' + str(username) + "\n")
            contact = {
                "email": email,
                "phone": "",
                "address": "",
                },
            TeamMember.objects.filter(user=request.user).create(
                user_id = request.user.id,
                user_name = username,
                contact = contact,
                authorised = False,
                designation = "Member",
                )
            request.session['msg']=''
        else:
            request.session['msg']='pass_not_match'
            print("\n Password fields didn't match. \n")
            return redirect('/authorization')
    else:
        print("\n Somthing Wrong Happened. \n")
        request.session['msg']=''
        return HttpResponse('<h2>Something Wrong Happened </h2>')
    request.session['msg']=''
    return redirect('/user/edit')


#Functions defination ends here