import json
import os
import requests
import logging
from marketdata.derivatives import Derivatives
from marketdata.moneymarkets import MoneyMarkets
from marketdata.spotprices import SpotPrices
from curvedata.forward_curves import ForwardCurves
from os.path import join, dirname
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(message)s',
                    handlers=[logging.FileHandler("energydesk_client.log"),
                              logging.StreamHandler()])

def load_env():
    logging.info("Loading environment")
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)

if __name__ == '__main__':
    load_env()
    token = os.environ.get("basic_auth_token")
    server_url = os.environ.get("server_url")
    price=ForwardCurves.get_period_price(server_url, token, "2023-01-01", "2025-01-01", "NO1", "EUR")
    print("Curve price is ", price)

    df = ForwardCurves.get_hourly_price_curve(server_url, token, "2023-01-01", "2025-01-01", "NO1", "EUR")
    print(df)
    df.index=df['date']
    # Pandas re sapling  YS=startof year, QS=startof quarter, MS=startofmonth, W =Week
    df = df.resample("MS").mean()
    df['EURNOK'] = 10 #eurnok
    df['rate'] = 0.05  # Interest rate
    print(df)
    # markets=Derivatives.fetch_markets(server_url, token)
    # print(markets)
    # df=Derivatives.fetch_product_prices(server_url, token, "Nasdaq OMX", "Nordic Power", "NO1")
    # print(df)
    # df=Derivatives.fetch_daily_prices(server_url, token, "Nasdaq OMX", "Nordic Power", "NO1")
    # print(df)
    # df=MoneyMarkets.fetch_forex_spot_rates(server_url, token)
    # print(df)
    # df=MoneyMarkets.fetch_zero_coupon_rates(server_url, token)
    # print(df)
    # df=SpotPrices.fetch_spot_prices(server_url, token, "Nord Pool", "2022-01-01", "2022-06-01")
    # print(df)