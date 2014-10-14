from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from django.template.context import RequestContext
from trade.models import Trade
from trade.forms import TradeForm
from django.http import HttpResponseRedirect


def index(request):
    allTrades = Trade.objects.all()
    context = RequestContext(request, {'allTrades': allTrades})
    return render(request, 'trade/index.html', context)


def new(request):
    form = TradeForm()
    return render(request, 'trade/new.html', {'form': form})


@csrf_protect
def insert(request):
    if request.method == "POST":
        form = TradeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
            return HttpResponseRedirect('/Trade/')

def delete(request,id):
    trade = Trade.objects.get(pk=id)
    trade.delete()
    return index(request)

