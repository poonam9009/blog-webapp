from django.shortcuts import render,HttpResponse, redirect,reverse
#USING THE DEFUALT USER MODEL.
from django.contrib.auth.models import User
from home.models import Contacthtmldata
from blog.models import BlogAppPost
from django.contrib import messages

def index(request):
    allpost = BlogAppPost.objects.all()
    context = {'allpost':allpost}
    return render(request,'home/home.html' ,{'allpost':allpost})


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')
        if len(name)<=0 and len(phone)<10 and len(email)<9 and len(desc)<2:
            messages.error(request, " please fill the form correctly")
        else :
            contacts= Contacthtmldata(name=name, email=email, phone=phone, desc=desc)
            contacts.save()
            messages.success(request,"Your message has been sent successfully.")
    return render(request,'home/contact.html')


def about(request):
    return render(request,'home/about.html')


def search(request):
    search = request.GET['search']
    if len(search) > 78:
        allpost = BlogAppPost.objects.none()
    else :
        allpostitle = BlogAppPost.objects.filter(title__icontains=search)
        allpostcontent = BlogAppPost.objects.filter(content__icontains=search)
        allpostauthor = BlogAppPost.objects.filter(author__icontains = search)
        allpostone = allpostitle.union(allpostcontent)
        allpost = allpostone.union(allpostauthor)
    params = {'allpost':allpost, 'search':search}
    return render(request,'home/search.html',params)
