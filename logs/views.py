from django.contrib.auth.models import User
from django.shortcuts import render,HttpResponse, redirect,reverse
#USING THE DEFUALT USER MODEL.
from home.models import Contacthtmldata
from blog.models import BlogAppPost
from django.contrib import messages

# Create your views here.

def signup(request):
    if request.method == "POST":
        name = request.POST.get('name')
        last = request.POST.get('last')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User()
        user.first_name = name
        user.last_name = last
        user.username = email
        user.email = email
        user.save()

        user.set_password(password)
        user.save()
        messages.success(request, "your account has been created successfully !!")
        return redirect(
            reverse('signup')
        )
    else:
        return render(
            request,
            "signup.html"
        )

def profile(request):
    return redirect('/home/')