# Generated by Django 3.1.3 on 2020-12-28 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0004_auto_20201228_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FilePathField(default='', path='/static/img'),
        ),
    ]
