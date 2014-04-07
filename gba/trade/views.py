import datetime
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from django.template.context import RequestContext
from competition.models import Competition
from market.models import Market
from team.models import Team
from trade.models import Trade

def index(request):
    allTrades = Trade.objects.all()
    context = RequestContext(request, {'allTrades': allTrades})
    return render(request, 'trade/index.html', context)

def new(request):
    allMarkets = Market.objects.all()
    context = RequestContext(request, {'allMarkets': allMarkets })
    return render(request, 'trade/new.html', context)

@csrf_protect
def insert(request):
    trade = Trade()
    trade.homeTeam = Team.objects.get(pk=request.POST.get('homeTeam'))
    trade.awayTeam = Team.objects.get(pk=request.POST.get('awayTeam'))
    trade.competition = Competition.objects.get(pk=request.POST.get('competition'))
    trade.market = Market.objects.get(pk=request.POST.get('market'))
    trade.invested = request.POST['invested']
    trade.profitLoss = request.POST['profitLoss']
    trade.date = datetime.datetime.now()
    trade.save()
    return render(request, 'trade/index.html', )