from django.shortcuts import render, HttpResponse
from Tournament_Registrations.models import *
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == 'POST':
        captain_email = request.POST.get('captain_email')
        football_team = Football_team.objects.all().filter(captain_email=captain_email)[0]
        team_size = football_team.__len__()
        team = ''
        for i in range(0,team_size):
            team+=request.POST.get('name-' + str(i+1))
            team+=','
            team+=request.POST.get('email-' + str(i+1))
            team+='\n'

        football_team.team = team
        football_team.save()
        messages.success(request, "Team Registered")
    return render(request, 'index.html')

def football(request):
    return render(request, 'football1.html')

def football_team(request):
    name = request.POST.get('captain_name')
    email = request.POST.get('captain_email')
    batch = request.POST.get('batch')
    team_name = request.POST.get('team_name')
    team_size = request.POST.get('team_size')

    football_team = Football_team(batch=batch, captain_name=name, captain_email=email, team_size=team_size, team_name=team_name)
    football_team.save()
    team_list = []
    for i in range(0,int(team_size)):
        team_list.append(i+1)

    context = {
        'captain': football_team,
        'team_size_list':team_list,
        'team_size':team_size
    }
    return render(request, 'football2.html', context=context)