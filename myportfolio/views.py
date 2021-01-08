from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader,Context
from .models import Project,Blog,Skill
# Create your views here.


def index(request):
    template = loader.get_template("myportfolio/index.html")
    projects = Project.objects.all()
    skills = Skill.objects.all()
    context={ 'projects' : projects,'skills':skills}
    return HttpResponse(template.render(context,request))


def experiences(request):
    return HttpResponse("you are in experience page")


def blogs(request):
    template = loader.get_template("myportfolio/blog.html")
    blogs = Blog.objects.all().order_by('-published_on')
    context = {'blogs': blogs}
    return HttpResponse(template.render(context, request))


def projects(request):
    return HttpResponse("you are in projects pages")