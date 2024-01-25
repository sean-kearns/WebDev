from django.urls import path 

from . import views #imporitng from current directory . 

#list of allowable urls that can be accessed by this app
urlpatterns = [
    #basically root path 
    path("", views.index, name = "index"), #no additonal path, views from views file and index is the name of the function being invoked
    path("brian", views.brian, name='brian'), #additonal path of /brian calles the other function, called brian 
    path("<str:name>", views.greet, name="greet")  #runs the greet function from the views.py file based on the string path in the url 
]