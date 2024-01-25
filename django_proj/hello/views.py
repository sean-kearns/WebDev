from django.shortcuts import render

from django.http import HttpResponse #package from Django, allows to give HHTP responses 

# Create your views here.
def index(request):
    #passing in an entire html page from the response in the hello/
    return render(request, "hello/index.html")

def brian(request):
    return HttpResponse("Hello, Brian!")

def greet_old(request, name):
    #takes an http request and a parameter to pass back that info 
    return HttpResponse(f"Hello, {name.capitalize()}!")

def greet(request, name):
    #pass vairables to html page 
    #giving the template access to a variable called name which is a parameter to this function 
    return render(request, "hello/greet.html", {
        "name":name.capitalize()
    })