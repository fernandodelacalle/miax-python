import pandas as pd 
import urllib 

# !export PYTHONHTTPSVERIFY=0
import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)): 
    ssl._create_default_https_context = ssl._create_unverified_context

def get_data_iex(symbol, st_range='5y'):
    base_url = 'https://api.iextrading.com/1.0'
    url = f'{base_url}/stock/{symbol}/chart/{st_range}'
    contents = urllib.request.urlopen(url).read()
    data = pd.read_json(contents)
    data = data[['date', 'open', 'high', 'low', 'close']]
    data = data.set_index('date', drop=True)
    return data
