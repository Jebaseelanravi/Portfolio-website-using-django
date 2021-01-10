from django.db import models
import os
# Create your models here.
from django.conf import settings
from datetime import date,datetime

class Project(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=2000)
    github_link = models.CharField(max_length=2000)
    tech_stack = models.CharField(max_length=500)
    image = models.FilePathField(path=os.path.join(settings.BASE_DIR, "myportfolio/static/img"), default="")

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=500)
    link = models.CharField(max_length=2000)
    published_on = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title


class Experience(models.Model):
    designation = models.CharField(max_length=500)
    start_date = models.DateField()
    end_date = models.DateField(blank=True)
    is_present = models.BooleanField(null=True,blank=True)
    responsibilities_1 = models.CharField(max_length=2000,default=None,blank=True)
    responsibilities_2 = models.CharField(max_length=2000,default=None,blank=True)
    responsibilities_3 = models.CharField(max_length=2000,default=None,blank=True)
    responsibilities_4 = models.CharField(max_length=2000,default=None,blank=True)
    company = models.CharField(max_length=200,default=None,blank=True)
    location = models.CharField(max_length=200,default=None,blank=True)


    def __str__(self):
        return self.designation


class Skill(models.Model):

    name = models.CharField(max_length=50)
    image =models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Connection(models.Model):
    your_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.your_name


class Profile(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=500)
    summary = models.CharField(max_length=5000)
    image = models.FilePathField(path=os.path.join(settings.BASE_DIR, "myportfolio/static/img"), default="")
    phone_number = models.CharField(max_length=100)
    email = models.EmailField()
    fb_link = models.URLField()
    github_link = models.URLField()
    insta_link = models.URLField()
    linkedin_link = models.URLField()


    def __str__(self):
        return self.name
