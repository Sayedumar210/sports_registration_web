from django.contrib import admin
from django.urls import path, include
from Tournament_Registrations import views

urlpatterns = [
    path('', views.index, name='index'),
    path('football', views.football, name='football'),
    path("football_team", views.football_team, name="football_team")
]