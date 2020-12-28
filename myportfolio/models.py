from django.db import models
import os
# Create your models here.
from django.conf import settings


class Project(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=2000)
    github_link = models.CharField(max_length=2000)
    tech_stack = models.CharField(max_length=500)
    image = models.FilePathField(path= os.path.join(settings.BASE_DIR,"myportfolio/static/img"), default="")

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=500)
    link = models.CharField(max_length=2000)

    def __str__(self):
        return self.title


class Experience(models.Model):
    designation = models.CharField(max_length=500)
    start_date = models.DateField()
    end_date = models.DateField()
    responsibilities = models.CharField(max_length=2000)

    def __str__(self):
        return self.designation
