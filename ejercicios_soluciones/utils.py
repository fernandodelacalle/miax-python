import pandas as pd 
import urllib 


TOKEN = None


def get_data_iex(symbol, st_range = '5y'):
    if not TOKEN:
        raise Exception('Pon tu token en utils.py')
        
    base_url = 'https://cloud.iexapis.com/stable'
    url = f'{base_url}/stock/{symbol}/chart/{st_range}?token={TOKEN}'
    contents = urllib.request.urlopen(url).read()
    data = pd.read_json(contents)
    data = data[['date', 'open', 'high', 'low', 'close']]
    data = data.set_index('date', drop=True)
    return data
