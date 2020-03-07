import abc
from ..models import Stock


class Ticker(abc.ABC):
    def load_new_series(self, symbol):
        data = self.fetch_series(symbol)
        stock = Stock(company=symbol)
        stock.save()

        for date, time_series in data.items():
            stock.quote_set.create(
                time_stamp=date,
                open=time_series['open'],
                close=time_series['close'],
                high=time_series['high'],
                low=time_series['low'],
                volume=time_series['volume']
            )

    @abc.abstractmethod
    def fetch_series(self, symbol):
        pass
