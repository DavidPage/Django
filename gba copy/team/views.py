from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from team.models import Team


def index(request):
    allTeams = Team.objects.all()
    context = RequestContext(request,
                             {'allTeams': allTeams}
    )
    return render(request, 'team/index.html', context)

def new(request):
    return render(request, 'team/new.html', )

def insert(request):
    if request.method == 'POST': # If the form has been submitted...
        t = Team(team_name=request.POST["teamName"])
        t.save()
        return HttpResponseRedirect('/Team/')