import httpx
import json
import os
import pandas as pd
from io import StringIO
import pathlib
import asyncio
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

SYMBOL_LIST = ['TSLA', 'AAPL', 'ATVI', 'SPG', 'BA', 'CCL', 'LB', 'SPR', 'FB', 'M', 'MAC', 'BABA', 'DAL', 'JPM', 'MA',
               'MSFT', 'NEM', 'SAVE']

DATA_PATH = '../data'
INTERVAL = '1min'

symbol_amount = len(SYMBOL_LIST)

# FIXME Ограничение 5 вызовов в минуту!
with open('keys.json', 'r', encoding='utf8') as file:
    KEYS = json.load(file)

queue = asyncio.Queue()


async def start():
    for symbol in SYMBOL_LIST:
        await queue.put(symbol)

    await asyncio.sleep(0.5)

    workers = list()
    for i, token in enumerate(KEYS):
        workers.append(asyncio.create_task(worker(i, token)))
    await asyncio.gather(*workers)
    print('Control sum:', symbol_amount)


async def worker(worker_id: int, token):
    async with httpx.AsyncClient() as client:
        tasks = list()
        counter = 0
        while True:
            if not queue.empty():
                symbol = await queue.get()
            else:
                break
            if counter >= 5:
                counter = 0
                await asyncio.gather(*tasks)
                tasks = list()
                await asyncio.sleep(60)
            tasks.append(asyncio.create_task(mine_symbol(worker_id, client, symbol, token)))
            counter += 1
        await asyncio.gather(*tasks)
        logging.info(f"Mined all. Shut down worker {worker_id}...")


async def mine_symbol(worker_id: int, client: httpx.AsyncClient, symbol: str, token: str, retries=5):
    p = pathlib.Path(f"{DATA_PATH}/{symbol}/")
    p.mkdir(parents=True, exist_ok=True)
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&' \
          f'symbol={symbol}&interval={INTERVAL}&apikey={token}&datatype=csv&outputsize=full'
    mined = False
    for i in range(retries):
        try:
            response = await client.get(url)
            table = response.content.decode('utf-8')
            data = pd.read_csv(StringIO(table), sep=',').iloc[::-1]
            time_column = pd.to_datetime(data['timestamp']).dt.strftime('%Y-%m-%d')

        except (KeyError, httpx.ConnectTimeout) as e:
            logging.warning(f'Worker {worker_id} is retrying {symbol}. Retries left: {retries - i}')
            await asyncio.sleep(60)

        else:
            data.to_csv(p / f'{time_column.head(1).values[0]}_to_{time_column.tail(1).values[0]}.csv', index=False)
            mined = True
            logging.info(f'Worker {worker_id}: Completed {symbol}')

        if mined:
            break

    global symbol_amount
    symbol_amount -= 1

if __name__ == '__main__':
    asyncio.run(start())
