import config
import csv

from binance.client import Client

client = Client(config.API_KEY, config.API_SECRET)

prices = client.get_all_tickers()

for price in prices:
    print(price)

candles = client.get_klines(
    symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_15MINUTE)

csvfile = open('BTCUSDT_5min_012015-current.csv', 'w', newline='')
candlestick_writer = csv.writer(csvfile, delimiter=',')

"""
for candlestick in candles:
    print(candlestick)

    candlestick_writer.writerow(candlestick)

print(len(candles))
"""

# fetch 1 minute klines for the last day up until now
candlesticks = client.get_historical_klines(
    "BTCUSDT", Client.KLINE_INTERVAL_5MINUTE, "1 Jan, 2017", "1 Nov, 2020", limit=1000)

for candlestick in candles:
    print(candlestick)

    candlestick_writer.writerow(candlestick)

csvfile.close()
