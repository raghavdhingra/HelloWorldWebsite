from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from main.serializer import MemberSerialiser
from rest_framework import status
import json
import requests
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User,Group
from main.models import TeamMember

# Create your views here.
def TeamUrlData():
    try:
        data = requests.get('http://dietitioapp.herokupp.com/home/v1/clinic_blogs/?p_id=207',headers = {"Authorization":'24619466-52bf-11e9-80da-9cad975b038d'})
        resp = json.loads(data.text)
    except:
        data = requests.get('http://127.0.0.1:8000/teamapi')    
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
    context = {
        "title":"Authorization",
        "meta_title":"LogIn / SignUp",
        "meta_description":"You can Login or SignUp through this on the HELLO WORLD Site"
    }
    return render(request,'auth.html',context)