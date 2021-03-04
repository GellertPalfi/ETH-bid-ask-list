import requests
import json


def get_okex_data():
    okex_data = requests.get('https://www.okex.com/api/spot/v3/instruments/ETH-USDT/book')
    okex_data_dict = json.loads(okex_data.text)
    return okex_data_dict


def get_binance_data():
    params = {
        'symbol': 'ETHUSDT',
        # 'limit': 100, documentation says default is 500 but in reality its 100
    }
    binance_data = requests.get('https://api.binance.com/api/v3/depth', params=params)
    binance_data_dict = json.loads(binance_data.text)
    return binance_data_dict


def merge():
    okex_data = get_okex_data()
    binance_data = get_binance_data()
    ask_values_okex = [index for index in okex_data['asks']]
    bid_values_okex = [index for index in okex_data['bids']]
    ask_values_binance = [index for index in binance_data['asks']]
    bid_values_binance = [index for index in binance_data['bids']]

    combined_ask_values = ask_values_okex + ask_values_binance
    combined_ask_values.sort()
    combined_bid_values = bid_values_okex + bid_values_binance
    combined_bid_values.sort()
    combined_bid_values.reverse()

    return combined_ask_values, combined_bid_values


merge()

