import pandas as pd 
import requests


TOKEN = None
BASE_URL = 'https://cloud.iexapis.com/stable'


def get_data_iex(symbol, st_range='1y'):
    url = f"{BASE_URL}/stock/{symbol}/chart/{st_range}"
    r = requests.get(url, params={'token': TOKEN, 'chartCloseOnly': True})
    data = pd.read_json(r.content)
    data = data.set_index('date')
    data = data.close
    data.name = symbol
    return data


