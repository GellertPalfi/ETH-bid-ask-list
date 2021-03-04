from django.shortcuts import render
from buy_sell.api_getter import merge

# Create your views here.


def sell(request):
    ask_list, _ = merge()  # merge returns 2 lists but only 1 of them is needed
    ask_list_dict = {
        'asks': ask_list
    }
    return render(request, 'sell.html', ask_list_dict)


def buy(request):
    _, bid_list = merge()  # same reason as in sell view
    bid_list_dict = {
        'bids': bid_list
    }
    return render(request, 'buy.html', bid_list_dict)
