# Create your views here.
from django.shortcuts import render
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
from competition.models import Competition


def index(request):
    competitions = Competition.objects.all()
    context = RequestContext(request,
                             {'allCompetitions': competitions}
    )
    return render(request, 'competition/index.html', context)

def new(request):
    return render(request, 'competition/new.html', )

def insert(request):
    competition = Competition(competition_name = request.POST.get('competitionName'))

    #competition.competition_name = request.POST.get('competitionName')
    competition.save()
    #return render('teste')
    return HttpResponseRedirect('/Competition/')