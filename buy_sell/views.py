from django.shortcuts import render
from buy_sell.api_getter import merge

# Create your views here.


def buy_sell(request):
    ask_list, bid_list = merge()  # merge returns 2 lists but only 1 of them is needed
    ask_list_dict = {
        'asks': ask_list,
        'bids': bid_list
    }
    return render(request, 'buy_sell.html', ask_list_dict)
