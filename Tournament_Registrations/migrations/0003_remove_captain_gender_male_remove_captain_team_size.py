# Generated by Django 4.2 on 2023-05-12 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tournament_Registrations', '0002_captain_remove_basketball_batch_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='captain',
            name='gender_male',
        ),
        migrations.RemoveField(
            model_name='captain',
            name='team_size',
        ),
    ]
