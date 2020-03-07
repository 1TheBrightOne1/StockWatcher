import urllib.request
import json
from datetime import datetime
from .Ticker import Ticker
import pytz


class AlphaVantage(Ticker):
    api_key = ''
    endpoint = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY'

    @staticmethod
    def fetch_series(symbol):
        url = AlphaVantage.endpoint + '&symbol=' + symbol + '&apikey=' + AlphaVantage.api_key
        doc = json.loads(urllib.request.urlopen(url).read())['Time Series (Daily)']
        out = {}
        for date, data in doc.items():
            timestamp = pytz.utc.localize(datetime.strptime(date, "%Y-%m-%d"))
            out[timestamp] = {}
            for key, value in data.items():
                out[timestamp][key.split(' ')[1]] = value

        return out


with open('./config.txt') as in_file:
    api_key = in_file.read()
