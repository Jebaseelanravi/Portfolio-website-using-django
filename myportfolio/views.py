from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader,Context
from .models import Project
# Create your views here.


def index(request):
    template = loader.get_template("myportfolio/index.html")
    projects = Project.objects.all()
    context={ 'projects' : projects}
    return HttpResponse(template.render(context,request))


def experiences(request):
    return HttpResponse("you are in experience page")


def blogs(request):
    return HttpResponse("you are in blogs pages")


def projects(request):
    return HttpResponse("you are in projects pages")