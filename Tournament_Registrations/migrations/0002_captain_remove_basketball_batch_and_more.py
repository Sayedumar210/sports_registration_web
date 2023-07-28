# Generated by Django 4.2 on 2023-05-11 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tournament_Registrations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Captain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch', models.IntegerField()),
                ('gender_male', models.BooleanField()),
                ('captain_email', models.EmailField(max_length=254)),
                ('captain_name', models.CharField(max_length=128)),
                ('team_size', models.IntegerField()),
                ('sport', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='basketball',
            name='batch',
        ),
        migrations.RemoveField(
            model_name='basketball',
            name='captain_email',
        ),
        migrations.RemoveField(
            model_name='basketball',
            name='captain_name',
        ),
        migrations.RemoveField(
            model_name='basketball',
            name='gender_male',
        ),
        migrations.RemoveField(
            model_name='basketball',
            name='team_size',
        ),
        migrations.RemoveField(
            model_name='cricket',
            name='batch',
        ),
        migrations.RemoveField(
            model_name='cricket',
            name='captain_email',
        ),
        migrations.RemoveField(
            model_name='cricket',
            name='captain_name',
        ),
        migrations.RemoveField(
            model_name='cricket',
            name='team_size',
        ),
        migrations.RemoveField(
            model_name='football',
            name='batch',
        ),
        migrations.RemoveField(
            model_name='football',
            name='captain_email',
        ),
        migrations.RemoveField(
            model_name='football',
            name='captain_name',
        ),
        migrations.RemoveField(
            model_name='football',
            name='team_size',
        ),
        migrations.RemoveField(
            model_name='volleyball',
            name='batch',
        ),
        migrations.RemoveField(
            model_name='volleyball',
            name='captain_email',
        ),
        migrations.RemoveField(
            model_name='volleyball',
            name='captain_name',
        ),
        migrations.RemoveField(
            model_name='volleyball',
            name='gender_male',
        ),
        migrations.RemoveField(
            model_name='volleyball',
            name='team_size',
        ),
    ]