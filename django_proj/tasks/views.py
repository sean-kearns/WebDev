from django.shortcuts import render
from django import forms 

from django.http import HttpResponseRedirect
from django.urls import reverse

from django.http import HttpResponse #package from Django, allows to give HHTP responses 

#tasks = ["foo", "bar", "baz"]

class NewTaskForm(forms.Form):
    task = forms.CharField(label = "New Task")
    #priority = forms.IntegerField(label="Priority", min_value=1, max_value=5)

# Create your views here.
def index(request):
    #looking in the session dictionrary for teh tasks object
    if "tasks" not in request.session:
        #if tasks not in there, then create it and make an empty list 
        request.session["tasks"] = []

    return render(request, "tasks/index.html",{
        "tasks": request.session["tasks"] 
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST) #request.POST contains all of the data that the user submitted on the form 
        if form.is_valid(): #if the form is valid, take some data from teh form and save it elsewhere 
            task = form.cleaned_data["task"]

            #tasks.append(task), isntead of this, adding to the variable in the page 
            request.session['tasks'] += [task]

            #now return to the index page if this is successful 
            return HttpResponseRedirect(reverse("tasks:index")) #uses a redirect funciton and a reverse function, uses url names to find the right urls 
        else:
            #the form variable now conatains what is wrong with the form that was initially submitted 
            return render(request, "tasks/add.html", {
                "form":form
            })


    return render(request, "tasks/add.html", {
        "form": NewTaskForm() #new task form object being created 
    })