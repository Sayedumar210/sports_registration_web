# Generated by Django 4.2 on 2023-05-13 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tournament_Registrations', '0003_remove_captain_gender_male_remove_captain_team_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='captain',
            name='team_name',
            field=models.CharField(default='none', max_length=50),
            preserve_default=False,
        ),
    ]