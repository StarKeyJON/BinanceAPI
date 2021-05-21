from flask import Flask, render_template, request, flash, redirect, jsonify
import config, csv, datetime
from binance.client import Client
from binance.enums import *

app = Flask(__name__)

client = Client(config.API_KEY, config.API_SECRET)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buy')
def buy():
    return 'buy'

@app.route('/sell')
def sell():
    return 'sell'

@app.route('/settings')
def settings():
    return 'settings'

@app.route('/history')
def history():
    candles = client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_15MINUTE)