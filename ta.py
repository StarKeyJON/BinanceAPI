import numpy
import talib
from numpy import genfromtxt

my_data = genfromtxt('BTC_BIN_15min.csv', delimiter=',')

print(my_data)

close = my_data[:,4]
print(close)
#moving_average = talib.SMA(close)
#
#from talib import MA_Type
#
#upper, middle, lower = talib.BBANDS(close, matype=MA_Type.T3)
#print(moving_average)
#print(upper, middle, lower)
rsi = talib.RSI(close)
print(rsi)