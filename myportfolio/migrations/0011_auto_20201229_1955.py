# Generated by Django 3.1.3 on 2020-12-29 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0010_auto_20201228_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FilePathField(default='', path='E:\\Python_workspace\\Portfolio-website-using-django\\myportfolio/static/img'),
        ),
    ]