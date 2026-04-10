from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Contact,SEO

# Create your views here.

def home(request):
    seo=SEO.objects.filter(page_name='home').first()
    return render(request, 'home.html',{'seo':seo})

def contact(request):
    seo=SEO.objects.filter(page_name='contact').first()
    if request.method=='POST':
        a=request.POST
        name=a.get('name')
        email=a.get('email')
        whatsapp=a.get('whatsapp')
        message=a.get('message')
        image=request.FILES.get('image')
        data=Contact(
            name=name,
            email=email,
            whatsapp=whatsapp,
            message=message,
            image=image
        )
        data.save()
        return JsonResponse({'message':'Your message has been sent successfully!'})

    return render(request, 'contact.html',{'seo':seo})


def login1(request):
    if request.user.is_authenticated:
        
        return redirect('premium')
    else:
        if request.method == "POST":
           a=request.POST
           name=a.get('name')
           password=a.get('password')
           user=authenticate(request,username=name,password=password)
           if user is not None:
                login(request,user)
                return redirect('premium')
           else:
                messages.error(request, "Invalid username or password")
    seo=SEO.objects.filter(page_name='login').first()
    return render(request, 'login.html',{'seo':seo})

def programs(request):
    seo=SEO.objects.filter(page_name='programs').first()
    return render(request, 'programs.html',{'seo':seo})

def about(request):
    seo=SEO.objects.filter(page_name='about').first()
    return render(request, 'about.html',{'seo':seo})

def support(request):
    seo=SEO.objects.filter(page_name='support').first()
    return render(request, 'support.html',{'seo':seo})