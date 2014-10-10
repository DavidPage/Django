from django.shortcuts import render
from django.template.context import RequestContext
from market.models import Market


def index(request):
    allMarkets = Market.objects.all()
    context = RequestContext(request,
                             {'allMarkets': allMarkets}
    )
    return render(request, 'market/index.html', context)

def new(request):
    return render(request, 'market/new.html', )

def insert(request):
    market = Market(market_name = request.POST.get('marketName'))
    market.save()
    return render(request, 'market/new.html', )