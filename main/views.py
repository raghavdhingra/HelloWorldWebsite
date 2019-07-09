from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        "title":"Hello World",
        "meta_title":"Hello World | GTBIT",
        "meta_description":"This is the official website of HELLO WORLD, GTBIT"
    }
    return render(request,'home.html',context)

def about(request):
    context = {
        "title":"Hello World",
        "meta_title":"Hello World | GTBIT",
        "meta_description":"This is the official website of HELLO WORLD, GTBIT"
    }
    return render(request,'about.html',context)

def contact(request):
    context = {
        "title":"Hello World",
        "meta_title":"Hello World | GTBIT",
        "meta_description":"This is the official website of HELLO WORLD, GTBIT"
    }
    return render(request,'contact.html',context)

def team(request):
    context = {
        "title":"Hello World",
        "meta_title":"Hello World | GTBIT",
        "meta_description":"This is the official website of HELLO WORLD, GTBIT"
    }
    return render(request,'team.html',context)

def event(request):
    context = {
        "title":"Hello World",
        "meta_title":"Hello World | GTBIT",
        "meta_description":"This is the official website of HELLO WORLD, GTBIT"
    }
    return render(request,'event.html',context)


