from django.shortcuts import render
from match.models import Match
from team.models import Team
from django.template.context import RequestContext
from competition.models import Competition
from django.http.response import HttpResponseRedirect
from forms import MatchForm

def index(request):
     matches = Match.objects.all()
     context = RequestContext(request, {'allMatches': matches})
     return render(request, 'match/index.html', context)

def new(request):
    #teams = Team.objects.all()
    #competitions = Competition.objects.all()
    #context = RequestContext(request, {'allTeams': teams, 'allCompetitions': competitions,})
    #return render(request, 'match/new.html',context )
    form = MatchForm()
    return render(request, 'match/new.html', {'form': form})

def insert(request):
    if request.method == 'POST': # If the form has been submitted...
        #postCompetition = Competition.objects.get(pk=request.POST["competition"])
        #postHomeTeam= Team.objects.get(pk=request.POST["homeTeam"])
        #postAwayTeam = Team.objects.get(pk=request.POST["awayTeam"])
        #m = Match(
        #    competition = postCompetition, homeTeam = postHomeTeam, awayTeam = postAwayTeam)
        #m.save()
        form = MatchForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
        return HttpResponseRedirect('/Match/')

    #return HttpResponseRedirect('/Match/')

def delete(request):
    if request.method == 'POST': # If the form has been submitted...
        m = Match.objects.get(pk=request.POST["match"])
        m.delete()
    return HttpResponseRedirect('/Match/')