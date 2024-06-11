'''
API Endpoints : Below are the available API resources:

GET /live
GET /live/{symbol}
GET /equities
GET /equities/{symbol}

'''

import requests
import pandas as pd
from datetime import datetime
import s3fs

def run_stock_etl():
    base_url = 'https://dev.kwayisi.org'
    url = f'{base_url}/apis/gse/live'
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for non-2xx status codes
    data = response.json()
    df = pd.DataFrame(data)
    
    df.to_csv("s3://bernard-airflow-gse-s3-bucket/stock_data.csv")