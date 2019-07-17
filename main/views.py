from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        "title":"Home | Hello World",
        "meta_title":"Hello World | GTBIT",
        "meta_description":"This is the official website of HELLO WORLD, GTBIT",
        "iterator": range(0,10)
    }
    return render(request,'home.html',context)

def about(request):
    context = {
        "title":"About | Hello World",
        "meta_title":"Hello World | GTBIT",
        "meta_description":"This is the official website of HELLO WORLD, GTBIT"
    }
    return render(request,'about.html',context)

def contact(request):
    context = {
        "title":"Contact | Hello World",
        "meta_title":"Hello World | GTBIT",
        "meta_description":"This is the official website of HELLO WORLD, GTBIT"
    }
    return render(request,'contact.html',context)

def team(request):
    context = {
        "title":"Team | Hello World",
        "meta_title":"Hello World | GTBIT",
        "meta_description":"This is the official website of HELLO WORLD, GTBIT"
    }
    return render(request,'team.html',context)

def event(request):
    context = {
        "title":"Events | Hello World",
        "meta_title":"Hello World | GTBIT",
        "meta_description":"This is the official website of HELLO WORLD, GTBIT"
    }
    return render(request,'event.html',context)


