#Imports statement
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from main.serializer import MemberSerialiser
from rest_framework import status
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
import json
import requests
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User,Group
from main.models import TeamMember

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
        data = requests.get('http://hello-world15.herokuapp.com/teamapi')
        resp = json.loads(data.text)
        print("\n\n Data is Fetch From Main API\n")
    except:
        data = requests.get('http://127.0.0.1:8000/teamapi')    
        resp = json.loads(data.text)
        print("\n\n Data is Fetched from Local API \n\n")
    return resp

def MemberDetails(userId):
    try:
        url = "http://hello-world15.herokuapp.com/teamapi/id=" + str(int(userId) + 2)
        data = requests.get(url)
        resp = json.loads(data.text)
    except:
        url = "http://127.0.0.1:8000/teamapi/id=" + str(int(userId) + 2)
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

class SingleMember(APIView):
    def get(self,UserId):
        member = TeamMember.objects.filter(pk = UserId)
        serializer = MemberSerialiser(member, many=True)
        return JsonResponse(serializer.data,safe=False)

    def post(self):
        pass

# Classes Ends


#Functions are defined here

def testUrl(request):
    try:
        data = requests.get('http://dietitioapp.herokupp.com/home/v1/clinic_blogs/?p_id=207',headers = {"Authorization":'24619466-52bf-11e9-80da-9cad975b038d'})
        resp = json.loads(data.text)
    except:
        data = requests.get('http://127.0.0.1:8000/teamapi')    
        resp = json.loads(data.text)
    print(resp)
    return JsonResponse(resp,safe=False)


def auth(request):
    username = ""
    if request.user.is_authenticated:
        data = MemberDetails(request.user.id)
        username = data[0]['first_name']
        if username == '':
            username = request.user.username
    context = {
        "title":"Authorization",
        "meta_title":"LogIn / SignUp",
        "meta_description":"You can Login or SignUp through this on the HELLO WORLD Site",
        "username": username,
    }
    return render(request,'auth.html',context)

@login_required
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
        #try:
        user = authenticate(request, username=username, password=password)
        if user is not None:
            request.session['msg']=''
            if core == 'on':
                print("\n Core Member Requested to Login. \n")
                check_auth = TeamMember.objects.filter(user_name=username)[0].authorised
                if check_auth == True:
                    print('\n You are a Core Member. \n')
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
            return redirect('/user/profile')
            
        # except Exception as e:
        #     print("\n" + str(e) + "\n")
        #     return HttpResponse("<h1>Some Error Has Been Occured</h1>")
        
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
            TeamMember(user = new_user).save()
            user = authenticate(username = username, password = password)
            login(request,user)
            print("\n" + 'successfully Logined as ' + str(username) + "\n")
            TeamMember.objects.filter(user = User.objects.get(pk = request.user.id)).update(user_name = username)

        else:
            request.session['msg']='pass_not_match'
            print("\n Password fields didn't match. \n")
            return redirect('/authorization')

    else:
        print("\n Somthing Wrong Happened. \n")
        return HttpResponse('<h2>Something Wrong Happened </h2>')
        
    return redirect('/user/edit')


#Functions defination ends here