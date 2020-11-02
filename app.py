from flask import Flask, render_template
import config
import csv
from binance.client import Client

app = Flask(__name__)

client = Client(config.API_KEY, config.API_SECRET)


@app.route('/')
def index():
    title = 'CoinView'

    info = client.get_account()
    balances = info['balances']

    exchange_info = client.get_exchange_info()
    symbols = exchange_info['symbols']

    return render_template('index.html', title=title, my_balances=balances, symbols=symbols)


@app.route('/buy')
def buy():
    return 'buy'


@app.route('/sell')
def sell():
    return 'sell'


@app.route('/settings')
def settings():
    return 'settings'
