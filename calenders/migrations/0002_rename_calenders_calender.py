# Generated by Django 4.2.5 on 2023-09-09 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0001_initial'),
        ('calenders', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Calenders',
            new_name='Calender',
        ),
    ]