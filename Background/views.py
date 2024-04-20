from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def landing(req):
    return render(req, "remove.html")

def upload(req):
    return render(req, "upload.html")

def login(req):
    return render(req, "login.html")

def signup(req):
    return render(req, "signup.html")
   


