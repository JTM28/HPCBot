import requests

from src.datastream.util import create_url




class BaseStream:

    def __init__(self):
        pass


    @property
    def http_url(self):
        raise NotImplementedError

    @property
    def wss_url(self):
        raise NotImplementedError


class BinanceApi:
    _http = 'https://fapi.binance.com/fapi/v1/'
    _wss = 'wss://fstream.binance.com'



    @property
    def http_url(self):
        return self._http

    @property
    def wss_url(self):
        return self._wss


r = requests.get('https://fapi.binance.com/fapi/v1/exchangeInfo')

print(r.text)

