from django.shortcuts import render,reverse
from django.http import HttpResponseRedirect
from .models import *
import json

def home(request):
    owner = Owner.objects.first()
    about = About.objects.first()
    testimonials = Testimonial.objects.all()
    services = Service.objects.all()
    clients = Client.objects.all()
    funfact = Funfact.objects.first()
    sociallinks = sociallink.objects.first()
    resume = Resume.objects.first()
    educations = Education.objects.all()
    experiences = Experience.objects.all()
    skills = Skill.objects.all()
    portfolios = Portfolio.objects.all()
    contactdetail = ContactDetail.objects.first()
    return render(request,"index.html",{'owner':owner,'about':about,'testimonials':testimonials,'services':services,
                                        'clients':clients,'funfact':funfact,'sociallink':sociallinks,'resume':resume,
                                        'educations':educations,'experiences':experiences,'skills':skills,
                                        'portfolios':portfolios,'contactdetail':contactdetail,})

def portfolioview(request,pk):
    portfolio = Portfolio.objects.get(id=pk)
    return render(request,"portfolio-1.html",{'portfolio':portfolio,'technology_list': portfolio.technology.split(",")})

def contactform(request):
    if request.POST:
        print(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact.objects.create(name=name,email=email,message=message)
        contact.save()
        return HttpResponseRedirect(reverse('home'))
    return render(request,'index.html',{})