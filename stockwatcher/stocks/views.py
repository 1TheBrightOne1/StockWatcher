from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import WatchNewStock
from .models import Stock
from .tickers.AlphaVantage import AlphaVantage


def index(request):
    form = WatchNewStock()
    return render(request, 'stocks/index.html', {'form':form})


def watch(request):
    if request.method == 'GET':
        form = WatchNewStock()

    else:
        form = WatchNewStock(request.POST)
        if form.is_valid():
            company = request.POST['company_name']
            api = AlphaVantage()
            api.load_new_series(company)
            return HttpResponseRedirect('/stocks')

    context = {
        'form': form
    }

    return render(request, 'stocks/index.html', context)
