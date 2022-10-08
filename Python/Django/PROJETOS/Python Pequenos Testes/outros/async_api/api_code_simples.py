import requests 
import os

api_key = os.getenv('ALPHAVANTAGE_API_KEY')
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={}&interval=5min&apikey={}'
symbols = ['APPL', 'GOOG', 'TSLA', 'MSFT', 'APPL', 'GOOG', 'TSLA', 'MSFT']
results = []

for symbol in symbols:
    print('Working on symbol {}'.format(symbol))
    response = requests.get(url.format(symbol, api_key))
    results.append(response.json())
print('A tarefa terminou de ser executada!')

# Ver na doc sobre api keys e variaveis internas
# Checar no arquivo async_api_code para ver a versão asyncrona