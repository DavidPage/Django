from django.shortcuts import render
from match.models import Match
from django.template.context import RequestContext

def index(request):
     matches = Match.objects.all()
     context = RequestContext(request,{'allMatches': matches})
     return render(request, 'match/index.html', context)