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
from .models import *
from login.views import *
import json
import cloudinary
import cloudinary.uploader
import cloudinary.api
import requests

auth_user = ["Siddharth","raghav","palak","prabhdeepsingh3499"]
auth_user_list = auth_user

# Create your views here.

def uploadFile(file):
    resp = cloudinary.uploader.upload(file)
    return resp['url']


def home(request):

    # For Inserting the Signed In Member In The Mailing List

    # mailList = []
    # oldMailList = Email.objects.filter(name = 'raghav')[0].email
    # mailList+=oldMailList
    # print(mailList)
    # meme = TeamMember.objects.all()
    # for mem in meme:
    #     if mem.contact['email'] in mailList:
    #         print("None")
    #     else:
    #         newMail = []
    #         newMail.append(mem.contact['email'])
    #         print(newMail)
    #         mailList+=newMail
    # Email.objects.filter(name = 'raghav').update(
    #     email = mailList
    # )

    ##################################################


    up_event = []
    past_event = []
    username = ""
    teamMember = TeamMember.objects.all()
    if request.user.is_authenticated:
        username = User.objects.filter(pk=request.user.id)[0].first_name
        if username == '':
            username = request.user.username
    
    events = Events.objects.all()
    for ent in events:
        if ent.upcoming == True:
            up_event.append(ent)
    for ent in events:
        if len(past_event) < 3:
            past_event.append(ent)
        else:
            break

    if up_event == []:
        up_event = ''
    context = {
        "title":"Home - HelloWorld",
        "meta_title":"Home - HelloWorld",
        "meta_description":"Welcome to the HelloWorld website. HelloWorld is the technical society of GTBIT. We aim to impart our knowledge and guidance to the young minds to create and improvise. HelloWorld is probably the first code of any language which once done provides with a sense of accomplishment and a thumbs up to the journey ahead.",
        "teamMembers": teamMember,
        "username": username,
        "developer":TeamMember.objects.filter(user_name='raghav')[0],
        "up_event": up_event,
        "past_event": past_event,
    }
    return render(request,'home.html',context)

def addEmailId(request):
    dict = {}
    if request.is_ajax:
        new_email = request.GET.get("emailId")
        emailList = Email.objects.filter(name = 'raghav')[0].email
        if new_email in emailList:
            print('This Email address is already in the mailing List.')
        else:
            emailList.append(new_email)
            print(new_email)
            Email.objects.filter(name='raghav').update(
                email = emailList,
            )
        return JsonResponse(json.dumps(dict),safe=False)
    else:
        return HttpResponse("<h1>Something Wrong Happened</h1>")

def about(request):
    username = ""
    if request.user.is_authenticated:
        username = User.objects.filter(pk=request.user.id)[0].first_name
        if username == '':
            username = request.user.username
    context = {
        "title":"About - HelloWorld",
        "meta_title":"About - HelloWorld",
        "meta_description":"Since the establishment of our team, we have created a team of minds with a varied skill set. Know more about us!",
        "username": username,
        "developer":TeamMember.objects.filter(user_name='raghav')[0],
    }
    return render(request,'about.html',context)

def gallery(request):
    data = requests.get("https://raw.githubusercontent.com/HelloWorldGTBIT/GalleryApi/master/gallery.json")
    resp = json.loads(data.text)
    galleryImages = resp['links']
    
    username = ""
    if request.user.is_authenticated:
        username = User.objects.filter(pk=request.user.id)[0].first_name
        if username == '':
            username = request.user.username
    context = {
        "title":"Gallery - HelloWorld",
        "meta_title":"Gallery - HelloWorld",
        "meta_description":"Since the establishment of our team, we have created a team of minds with a varied skill set. Know more about us!",
        "username": username,
        "developer":TeamMember.objects.filter(user_name='raghav')[0],
        "Images":galleryImages,
    }
    return render(request,'gallery.html',context)

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
        "title":"Contact - HelloWorld",
        "meta_title":"CONTACT US | HelloWorld",
        "meta_description":"Got an issue or suggestion? Reach out to us to share with us anything on your mind regarding us.",
        "username": username,
        "developer":TeamMember.objects.filter(user_name='raghav')[0],
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
        "meta_title":"Know Our Team | HelloWorld",
        "meta_description":"Since the establishment of our team, we have created a team of minds with a varied skill set. We work in various fields to develop and implement. We aren't just a team but a family sharing bonds and knowledge with a common aim to serve the era of globalisation and digitalization. Want to know more about our journey and plans ahead?",
        "username": username,
        "developer":TeamMember.objects.filter(user_name='raghav')[0],
        "teamMember": teamMember,
    }
    return render(request,'team.html',context)


def event(request):

    up_event = []
    past_event = []
    filter = ''

    username = ""
    if request.user.is_authenticated:
        username = User.objects.filter(pk=request.user.id)[0].first_name
        if username == '':
            username = request.user.username

    events = Events.objects.all()
    for ent in events:
        if ent.upcoming == True:
            up_event.append(ent)
        elif ent.upcoming == False:
            past_event.append(ent)


    if request.method == 'POST':
        select = request.POST.get('select')
        if select == 'upcoming Event':
            print('upcoming Event')
            filter = 'up'
        elif select == 'Past Event':
            print('Past Event')
            filter = 'past'
        else:
            print('all')

    if up_event == []:
        up_event = ''
    context = {
        "title":"Events | HelloWorld",
        "meta_title":"Events | HelloWorld",
        "meta_description":"Test your skills and keep your competitive spirits high, participate in our offline and online events conducted at regular intervals. Not to forget about the amazing goodies and merchandises which come along with the events! Sign up and login if you haven't done it yet to participate in our events!",
        "username": username,
        "developer":TeamMember.objects.filter(user_name='raghav')[0],
        "up_event": up_event,
        "past_event": past_event,
        "filter": filter,
    }
    return render(request,'event.html',context)


def hackgtbit(request):
    username = ""
    if request.user.is_authenticated:
        username = User.objects.filter(pk=request.user.id)[0].first_name
        if username == '':
            username = request.user.username

    timeline = Hackgtbit.objects.all()
    dayOne = []
    dayTwo = []

    timelineLength = len(timeline)
    for eve in range(1,20):
        if Hackgtbit.objects.filter(serial=eve):
            dayOne += Hackgtbit.objects.filter(serial=eve)
    
    for eve in range(21,40):
        if Hackgtbit.objects.filter(serial=eve):
            dayTwo += Hackgtbit.objects.filter(serial=eve)

    context = {
        "title":"Hack GTBIT 2.0 | HelloWorld",
        "meta_title":"Hack GTBIT 2.0 | HelloWorld",
        "meta_description":"H@ckGTBIT 2.0 isn't just an event for us,it is in fact a journey that has helped us to define ourselves, find our paths and most importantly take something from it to cherish as a team. Our aim is to let this event take the form of a platform which would help the students, faculty, participants and sponsors interact with each other and form bonds stronger than those made on paper.",
        "username": username,
        "developer":TeamMember.objects.filter(user_name='raghav')[0],
        "header": "Hack GTBIT 2.0",
        "dayOne":dayOne,
        "dayTwo":dayTwo,
    }
    return render(request,'hackgtbit2.html',context)


def profile(request):
    all_events = Events.objects.all()
    all_upEvents = []
    for e in all_events:
        if e.upcoming == True:
            all_upEvents.append(e)

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
            "developer":TeamMember.objects.filter(user_name='raghav')[0],
            "header": "Your Profile",
            "title": str(username) + " | Profile",
            "meta_title":"Profile | HelloWorld",
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
            "all_upEvents":all_upEvents,
            "auth_user_list":auth_user_list,
        }
    except:
        return HttpResponse("<center><h1>Access Denied</h1><h3>You are not allowed to access this tab</h3><h4>Only authorised user can have access to this page.</h4><h3>Go Back</h3></center>")
    return render(request,'profile.html',context)

def edit(request):
    all_events = Events.objects.all()
    all_upEvents = []
    for e in all_events:
        if e.upcoming == True:
            all_upEvents.append(e)
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
            college = college,
            degree = degree,
            passing_year = passing_year,
            links = links,
            skills = teamSkill,
            contact = contact,
            )

        return redirect('/user/profile')
    try:
        context = {
            "username":username,
            "auth_user_list":auth_user_list,
            "header": "Edit Your Profile",
            "developer":TeamMember.objects.filter(user_name='raghav')[0],
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
            "all_upEvents":all_upEvents,
        }
    except:
        return HttpResponse("<center><h1>Access Denied</h1><h3>You are not allowed to access this tab</h3><h4>Only authorised user can have access to this page.</h4><h3>Go Back</h3></center>")
    try:
        context['selectedIndex'] = interest_arr[1]
    except:
        context['selectIndex']= 0
    return render(request,'edit.html',context)

def changepassword(request):
    all_events = Events.objects.all()
    all_upEvents = []
    for e in all_events:
        if e.upcoming == True:
            all_upEvents.append(e)
    username = ""
    err = ""
    if request.user.is_authenticated:
        username = User.objects.filter(pk=request.user.id)[0].first_name
        if username == '':
            username = request.user.username
    context = {
        "username":username,
        "auth_user_list":auth_user_list,
        "header": "Change Your Password",
        "title": str(username) + " | Change Password",
        "meta_title":"Change Password | HelloWorld",
        "meta_description":"This is the official website of HELLOWORLD",
        "err":err,
        "developer":TeamMember.objects.filter(user_name='raghav')[0],
        "all_upEvents":all_upEvents,
    }
    return render(request,'changepassword.html',context)


def manageteam(request):
    all_events = Events.objects.all()
    all_upEvents = []
    for e in all_events:
        if e.upcoming == True:
            all_upEvents.append(e)
    if request.user.username in auth_user:
        username = ""
        if request.user.is_authenticated:
            username = User.objects.filter(pk=request.user.id)[0].first_name
            if username == '':
                username = request.user.username
        context = {
            "username": username,
            "developer":TeamMember.objects.filter(user_name='raghav')[0],
            "header": "Manage The Team",
            "title": str(username) + " | Team Management",
            "meta_title": "Manage Team | HelloWorld",
            "meta_description": "This is the official website of HELLOWORLD",
            "allTeam": User.objects.all(),
            "all_upEvents":all_upEvents,
            "auth_user_list":auth_user_list,
        }
        return render(request,'manageteam.html',context)
    else:
        return HttpResponse("<center><h1>Access Denied</h1><h3>You are not allowed to access this tab</h3><h4>Only authorised user can have access to this page.</h4><h3>Go Back</h3></center>")

def manageevent(request):
    all_events = Events.objects.all()
    all_upEvents = []
    for e in all_events:
        if e.upcoming == True:
            all_upEvents.append(e)
    if request.user.username in auth_user:
        username = ""
        if request.user.is_authenticated:
            username = User.objects.filter(pk=request.user.id)[0].first_name
            if username == '':
                username = request.user.username
        context = {
            "username": username,
            "developer":TeamMember.objects.filter(user_name='raghav')[0],
            "header": "Manage The Events",
            "title": str(username) + " | Event Management",
            "meta_title": "Manage Event | HelloWorld",
            "meta_description": "This is the official website of HELLOWORLD",
            "allEvent": Events.objects.all(),
            "all_upEvents":all_upEvents,
            "auth_user_list":auth_user_list,
        }
        return render(request,'manageevent.html',context)
    else:
        return HttpResponse("<center><h1>Access Denied</h1><h3>You are not allowed to access this tab</h3><h4>Only authorised user can have access to this page.</h4><h3>Go Back</h3></center>")


def single_member(request):
    slug = request.POST.get('postid')
    redirect_url = "/user/manage-team/user="+str(slug)
    return redirect(redirect_url)

def single_event(request):
    slug = request.POST.get('postid')
    redirect_url = "/user/manage-event/event="+str(slug)
    return redirect(redirect_url)

def post_by_username(request,slug):
    all_events = Events.objects.all()
    all_upEvents = []
    for e in all_events:
        if e.upcoming == True:
            all_upEvents.append(e)
    if request.user.username in auth_user:
        username = ""
        if request.user.is_authenticated:
            username = User.objects.filter(pk=request.user.id)[0].first_name
            if username == '':
                username = request.user.username
        user = TeamMember.objects.filter(user_name=slug)[0]
        context = {
            "userMember":user,
            "username": username,
            "header": user.first_name + "'s Changes",
            "developer":TeamMember.objects.filter(user_name='raghav')[0],
            "title": str(slug) + " | Edit",
            "meta_title": "User | HelloWorld",
            "meta_description": "This is the official website of HELLOWORLD",
            "all_upEvents":all_upEvents,
            "auth_user_list":auth_user_list,
        }
        return render(request,"single_member.html",context)
    else:
        return HttpResponse("<center><h1>Access Denied</h1><h3>You are not allowed to access this tab</h3><h4>Only authorised user can have access to this page.</h4><h3>Go Back</h3></center>")


def post_by_event(request,slug):
    all_events = Events.objects.all()
    all_upEvents = []
    for e in all_events:
        if e.upcoming == True:
            all_upEvents.append(e)
    if request.user.username in auth_user:
        username = ""
        if request.user.is_authenticated:
            username = User.objects.filter(pk=request.user.id)[0].first_name
            if username == '':
                username = request.user.username
        events = Events.objects.filter(id=slug)[0]
        context = {
            "event":events,
            "username": username,
            "header": events.name + "'s Changes",
            "developer":TeamMember.objects.filter(user_name='raghav')[0],
            "title": str(events.name) + " | Edit",
            "meta_title": "Event | HelloWorld",
            "meta_description": "This is the official website of HELLOWORLD",
            "all_upEvents":all_upEvents,
            "auth_user_list":auth_user_list,
        }
        return render(request,"single_event.html",context)
    else:
        return HttpResponse("<center><h1>Access Denied</h1><h3>You are not allowed to access this tab</h3><h4>Only authorised user can have access to this page.</h4><h3>Go Back</h3></center>")

def deleteevent(request):
    if request.method == 'POST':
        eventId = request.POST.get('eventid')
        Events.objects.filter(id = eventId).delete()
        return redirect("/user/manage-event")

def saveSingleEvent(request):
    if request.method == 'POST':
        eventId = request.POST.get('eventid')
        name = request.POST.get('name')
        date = request.POST.get('date')
        time = request.POST.get('time')
        location = request.POST.get('location')
        location_link = request.POST.get('location_link')
        desc = request.POST.get('description')
        registration_link = request.POST.get('registration_link')
        upcoming = request.POST.get('upcoming')
        if upcoming == 'on':
            check = True
        else:
            check = False
        
        Events.objects.filter(id = eventId).update(
            name = name,
            date = date,
            time = time,
            location = location,
            location_link = location_link,
            description = desc,
            registration_link = registration_link,
            upcoming = check,
        )

    return redirect("/user/manage-event")

def addevent(request):
    all_events = Events.objects.all()
    all_upEvents = []
    for e in all_events:
        if e.upcoming == True:
            all_upEvents.append(e)
    if request.user.username in auth_user:
        username = ""
        if request.user.is_authenticated:
            username = User.objects.filter(pk=request.user.id)[0].first_name
            if username == '':
                username = request.user.username
        
        if request.method == 'POST':
            name = request.POST.get('name')
            location = request.POST.get('location')
            date = request.POST.get('date')
            time = request.POST.get('time')
            event = Events.objects.create(name = name,location = location,date = date,time = time)
            return redirect('/user/manage-event/event={}'.format(event.id))
        context = {
            "username":username,
            "header": "Add New Event",
            "all_upEvents":all_upEvents,
            "title": str(username) + " | Add Event",
            "meta_title":"Add New Event | GTBIT",
            "meta_description":"This is the official website of HELLOWORLD",
            "developer":TeamMember.objects.filter(user_name='raghav')[0],
            "auth_user_list":auth_user_list,
        }
        return render(request,'addevent.html',context)
    else:
        return HttpResponse("<center><h1>Access Denied</h1><h3>You are not allowed to access this tab</h3><h4>Only authorised user can have access to this page.</h4><h3>Go Back</h3></center>")

def saveSingleEventImage(request):
    try:
        if request.method == 'POST':
            eventId = request.POST['eventid']
            try:
                if request.FILES['uploadFromPC']:
                    myimage = request.FILES['uploadFromPC']
                    resp = uploadFile(myimage)
                    Events.objects.filter(id = eventId).update(event_pic = resp)
                    return redirect('/user/manage-event/event={}'.format(eventId))
            except:
                return redirect('/user/manage-event')
    except:
        return redirect('/user/manage-event')
    return redirect("/user/manage-event")

def saveSingle(request):
    if request.method == 'POST':
        username = request.POST.get("userid")
        designation = request.POST.get("designation")
        core = request.POST.get("coremember")
        
        TeamMember.objects.filter(user_name = username).update(
            designation = designation,
        )
        if core == 'on':
            TeamMember.objects.filter(user_name = username).update(
                authorised = True,
            )
        elif core is None:
            TeamMember.objects.filter(user_name = username).update(
                authorised = False,
            )
    return redirect("/user/manage-team")

def resume(request):
    all_events = Events.objects.all()
    all_upEvents = []
    for e in all_events:
        if e.upcoming == True:
            all_upEvents.append(e)
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
        "meta_title":"Resume | GTBIT",
        "meta_description":"This is the official website of HELLOWORLD",
        "err":err,
        "developer":TeamMember.objects.filter(user_name='raghav')[0],
        "all_upEvents":all_upEvents,
        "auth_user_list":auth_user_list,
    }
    return render(request,'resume.html',context)

def uploadImage(request):
    myimage = request.FILES['uploadFromPC']
    if myimage is not None:
        resp = uploadFile(myimage)
        TeamMember.objects.filter(pk=request.user.id).update(profile_picture = resp)
    return redirect('/user/edit')

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

def code_of_conduct(request):
    username = ""
    if request.user.is_authenticated:
        username = User.objects.filter(pk=request.user.id)[0].first_name
        if username == '':
            username = request.user.username
    context = {
        "username":username,
        "header": "Code Of Conduct",
        "title": "Code Of Conduct | HelloWorld",
        "developer":TeamMember.objects.filter(user_name='raghav')[0],
        "meta_title":"HelloWorld | GTBIT",
        "meta_description":"This is the official website of HELLOWORLD",
    }
    return render(request,"conduct.html",context)

def terms_and_cond(request):
    username = ""
    if request.user.is_authenticated:
        username = User.objects.filter(pk=request.user.id)[0].first_name
        if username == '':
            username = request.user.username
    context = {
        "username":username,
        "developer":TeamMember.objects.filter(user_name='raghav')[0],
        "header": "Terms and Condition",
        "title": "Terms and Condition - HelloWorld",
        "meta_title":"Terms and Condition - HelloWorld",
        "meta_description":"This is the official website of HELLOWORLD",
    }
    return render(request,"terms.html",context)

def privacy_policy(request):
    username = ""
    if request.user.is_authenticated:
        username = User.objects.filter(pk=request.user.id)[0].first_name
        if username == '':
            username = request.user.username
    context = {
        "username":username,
        "header": "Privacy Policy",
        "developer":TeamMember.objects.filter(user_name='raghav')[0],
        "title": "Privacy Policy | HelloWorld",
        "meta_title":"Privacy Policy - HelloWorld",
        "meta_description":"This is the official website of HELLOWORLD",
    }
    return render(request,"privacy.html",context)

def faqs(request):
    username = ""
    if request.user.is_authenticated:
        username = User.objects.filter(pk=request.user.id)[0].first_name
        if username == '':
            username = request.user.username
    context = {
        "username":username,
        "header": "FAQs",
        "developer":TeamMember.objects.filter(user_name='raghav')[0],
        "title": "FAQs | HelloWorld",
        "meta_title":"FAQs | HelloWorld",
        "meta_description":"This is the official website of HELLOWORLD",
    }
    return render(request,"faq.html",context)

def error_404(request,exception):
    context = {}
    try:
        return render(request,'error404.html',context)
    except Exception as e:
        return HttpResponse(str(e) + "<Br>" + str(exception))

def error_500(request):
    context = {}
    try:
        return render(request,'error500.html',context)
    except Exception as e:
        return HttpResponse(e)