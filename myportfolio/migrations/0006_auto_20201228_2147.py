# Generated by Django 3.1.3 on 2020-12-28 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0005_auto_20201228_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FilePathField(default='', path='/myportfolio/static/img'),
        ),
    ]
