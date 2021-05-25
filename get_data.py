#from requests.models import CaseInsensitivDict
from sample_config import API_SECRET, API_KEY
import config, csv
from binance import Client

client = Client(config.API_KEY, config.API_SECRET)

print("API key secured")
#btc_price = client.get_symbol_ticker(symbol="BTCUSDT")

#prices = client.get_all_tickers()

#for price in prices:
#    print(price)

#candles = client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_5MINUTE)
candles = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_15MINUTE, "1 Jan, 2021", "25 Mar, 2021")

print("opening csv files")

csvfile = open('BTC_BIN_HIS_5min.csv', 'w', newline='')
#csvfile = open('BTC_BIN_HIST_5min.csv', 'w', newline='')

candlestick_writer = csv.writer(csvfile, delimiter=',')
#kline_writer = csv.writer(csvfile, delimiter=',')

for candlestick in candles:
    candlestick[0] = candlestick[0] / 1000
    candlestick_writer.writerow(candlestick)
#csvfile.close()

#for kline in klines:
#    kline_writer.writerow(kline)

csvfile.close()

#print(len(klines))

print("done")
