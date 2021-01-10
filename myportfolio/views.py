from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, Context
from .models import Project, Blog, Skill, Connection,Experience,Profile
# Create your views here.
from .forms import NameForm
from django.core.mail import send_mail


def index(request):
    template = loader.get_template("myportfolio/index.html")
    projects = Project.objects.all()
    skills = Skill.objects.all()
    experiences = Experience.objects.all().order_by('-start_date')[:5]
    profile = Profile.objects.all().first()
    form = NameForm()
    context = {'projects': projects, 'skills': skills, 'form': form,'experiences':experiences,'profile':profile}
    return HttpResponse(template.render(context, request))


def experiences(request):
    return HttpResponse("you are in experience page")


def blogs(request):
    template = loader.get_template("myportfolio/blog.html")
    blogs = Blog.objects.all().order_by('-published_on')
    context = {'blogs': blogs}
    return HttpResponse(template.render(context, request))


def contact(request):
    if request.method == 'POST':
        template = loader.get_template("myportfolio/contact.html")
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            ob = Connection()
            ob.your_name = form.cleaned_data['your_name']
            ob.email = form.cleaned_data['email']
            ob.subject = form.cleaned_data['subject']
            ob.message = form.cleaned_data['message']
            ob.save()
            context={}
            return HttpResponse(template.render(context, request))
            # return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return HttpResponseRedirect('/myportfolio')


def projects(request):
    return HttpResponse("you are in projects pages")
