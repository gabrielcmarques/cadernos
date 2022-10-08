import asyncio 
import aiohttp
import os

api_key = os.getenv('ALPHAVANTAGE_API_KEY')
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={}&interval=5min&apikey={}'
symbols = ['APPL', 'GOOG', 'TSLA', 'MSFT', 'APPL', 'GOOG', 'TSLA', 'MSFT']
results = []

async def get_symbols():
    async with aiohttp.ClientSession() as session:
        for symbol in symbols:
            print('Working on symbol {}'.format(symbol))
            response = await session.get(url.format(symbol, api_key))
            results.append(await response.json())

loop = asyncio.get_event_loop()
loop.run_until_complete(get_symbols())
loop.close()

# ou apenas asyncio.run(get_symbols()) vai executar essas 3 linhas acima em 1.

print('A tarefa terminou de ser executada!')