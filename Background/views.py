from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from .models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def landing(req):
    return render(req, "remove.html")

def upload(req):
    return render(req, "upload.html")

def login_view(req):
    if req.method == "POST":
       username = req.POST['username']
       password = req.POST['password']

       try:
          user = authenticate(username=username, password=password)

          if user== None:
             return render(req, "login.html", {'error': "Wrong Username or Password"})
          else:
             login(req, user=user)
             return HttpResponseRedirect("/")
       except:
        pass
          
    return render(req, "login.html")

def logout_view(req):
   logout(req)
   return HttpResponseRedirect("/")

def signup(req):
    if req.method == "POST":
        first_name = req.POST['first_name'] 
        last_name = req.POST['last_name'] 
        username = req.POST['username'] 
        password = req.POST['password'] 
        email = req.POST['email'] 

        try:
            User.objects.create_user(
                first_name= first_name,
                last_name= last_name,
                email= email,
                username= username,
                password= password)
            return HttpResponseRedirect("/")

        except:
          print("error")
          pass

    return render(req, "signup.html")
