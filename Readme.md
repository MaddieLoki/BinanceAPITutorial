# Informational URLs

## Tradingview Lightweight Charts Documentation

https://www.tradingview.com/lightweight-charts/

## Tradingview Lightweight Charts Github

https://github.com/tradingview/lightweight-charts

## Binance-Official-API-Docs github

https://github.com/binance-exchange/binance-official-api-docs

## Binance API Docs

https://binance-docs.github.io/apidocs/futures/en/#compressed-aggregate-trades-list

## Python-Binance documentation

https://python-binance.readthedocs.io/en/latest/

## Python Docs Library

https://docs.python.org/3/library/index.html

## TA-LIB Library

https://ta-lib.org/

## Python library downloads for Windows

https://www.lfd.uci.edu/~gohlke/pythonlibs/#ta-lib
https://blog.quantinsti.com/install-ta-lib-python/#windows

# Base URL for Web Socket Streams

wss://stream.binance.com:9443

### BTCUSDT streams

wss://stream.binance.com:9443/ws/btcusdt@trade
wss://stream.binance.com:9443/ws/btcusdt@kline_5m

### Trade Streams

The Trade Streams push raw trade information; each trade has a unique buyer and seller.

Stream Name: <symbol>@trade

Update Speed: Real-time

Payload:

{
"e": "trade", // Event type
"E": 123456789, // Event time
"s": "BNBBTC", // Symbol
"t": 12345, // Trade ID
"p": "0.001", // Price
"q": "100", // Quantity
"b": 88, // Buyer order ID
"a": 50, // Seller order ID
"T": 123456785, // Trade time
"m": true, // Is the buyer the market maker?
"M": true // Ignore
}

### Kline/Candlestick Streams

The Kline/Candlestick Stream push updates to the current klines/candlestick every second.

Kline/Candlestick chart intervals:

m -> minutes; h -> hours; d -> days; w -> weeks; M -> months

1m
3m
5m
15m
30m
1h
2h
4h
6h
8h
12h
1d
3d
1w
1M
Stream Name: <symbol>@kline\_<interval>

Update Speed: 2000ms

Payload:

{
"e": "kline", // Event type
"E": 123456789, // Event time
"s": "BNBBTC", // Symbol
"k": {
"t": 123400000, // Kline start time
"T": 123460000, // Kline close time
"s": "BNBBTC", // Symbol
"i": "1m", // Interval
"f": 100, // First trade ID
"L": 200, // Last trade ID
"o": "0.0010", // Open price
"c": "0.0020", // Close price
"h": "0.0025", // High price
"l": "0.0015", // Low price
"v": "1000", // Base asset volume
"n": 100, // Number of trades
"x": false, // Is this kline closed?
"q": "1.0000", // Quote asset volume
"V": "500", // Taker buy base asset volume
"Q": "0.500", // Taker buy quote asset volume
"B": "123456" // Ignore
}
}
