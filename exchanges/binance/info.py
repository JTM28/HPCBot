from time import time

from exchanges.main import get


BASE_HTTP_URL = 'https://fapi.binance.com/fapi/v1/'

INFO_URL = 'https://fapi.binance.com/fapi/v1/exchangeInfo'


doc = {
    'exchange': str,
    'pair': str,
    'base': str,
    'quote': str,
    'prec': {
        'base': int,
        'quote': int,
        'price': int,
        'qty': int
    }

}



def get_pairs():
    r = get('https://fapi.binance.com/fapi/v1/exchangeInfo')
    obj = r['symbols']
    record = {'exchange': 'binance', 'last-updated': time(), 'info': {}, 'pairs': {}}
    for each in obj:
        record['pairs'][each['symbol']] = {
            'base': each['baseAsset'],
            'quote': each['quoteAsset'],
            'prec': {
                'base': each['baseAssetPrecision'],
                'quote': each['quotePrecision'],
                'price': each['pricePrecision'],
                'qty': each['quantityPrecision']
            },
            'status': each['status']
        }
    record['info']['pairs'] = len(list(record['pairs'].keys()))
    record['info']['limits'] = {}
    return record
