from django.shortcuts import render
from models import Match

def index(request):
    competitions = Match.objects.all()
    context = RequestContext(request,
                             {'allMatches': matches}
    )
    return render(request, 'match/index.html', context)