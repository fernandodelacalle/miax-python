import pandas as pd 
import requests


TOKEN = None
BASE_URL = 'https://cloud.iexapis.com/stable'

def get_data_iex(symbol, st_range='1y'):
    if not TOKEN:
        raise Exception('Pon tu token en utils.py')
    url = f"{BASE_URL}/stock/{symbol}/chart/{st_range}"
    r = requests.get(url, params={'token': TOKEN}) #  'chartCloseOnly': True
    data = pd.read_json(r.content)
    data = data[['date', 'open', 'high', 'low', 'close']]
    data = data.set_index('date')
    return data
