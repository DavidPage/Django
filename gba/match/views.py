from django.shortcuts import render
from match.models import Match
from team.models import Team
from django.template.context import RequestContext

def index(request):
     matches = Match.objects.all()
     context = RequestContext(request, {'allMatches': matches})
     return render(request, 'match/index.html', context)

def new(request):
    teams = Team.objects.all()
    context = RequestContext(request, {'allTeams': teams})
    return render(request, 'match/new.html',context )