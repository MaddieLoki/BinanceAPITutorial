import numpy
import talib as ta
from numpy import genfromtxt

my_data = genfromtxt('BTCUSDT_15min.csv', delimiter=',')
# print(my_data)

close = my_data[:, 4]
# print(close)

output = ta.RSI(close, timeperiod=14)
print(output)
