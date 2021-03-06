from django.shortcuts import render, redirect
from buy_sell.api_getter import clean_data

# Create your views here.


def buy_sell(request):
    ask_list, bid_list = clean_data()  # merge returns 2 lists but only 1 of them is needed
    ask_list_dict = {
        'asks': ask_list,
        'bids': bid_list
    }
    return render(request, 'buy_sell.html', ask_list_dict)


def home_view(request):
    return redirect(buy_sell)
