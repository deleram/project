# Generated by Django 3.1.7 on 2021-03-07 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainone', '0013_studentexercises_numberexcer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentexercises',
            name='numberassignment',
        ),
    ]
