from django.shortcuts import render
from match.models import Match
from team.models import Team
from django.template.context import RequestContext
from competition.models import Competition


def index(request):
     matches = Match.objects.all()
     context = RequestContext(request, {'allMatches': matches})
     return render(request, 'match/index.html', context)

def new(request):
    teams = Team.objects.all()
    competitions = Competition.objects.all()
    context = RequestContext(request, {'allTeams': teams, 'allCompetitions': competitions,})
    return render(request, 'match/new.html',context )