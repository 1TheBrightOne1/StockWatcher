from django.shortcuts import render
from django.http import HttpResponse
from .forms import WatchNewStock
from .models import Stock


def index(request):
    return HttpResponse("hello there")


def watch(request):
    if request.method == 'GET':
        form = WatchNewStock()

    else:
        form = WatchNewStock(request.POST)
        stock = Stock(company=request.POST['company_name'])
        stock.save()

    context = {
        'form': form
    }

    return render(request, 'stocks/watch.html', context)
