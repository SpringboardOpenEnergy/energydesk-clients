import requests
import json
import logging
import pandas as pd
import pandas as pd
import pytz
from datetime import datetime, timedelta, timezone
import datetime as datetimetype
from django.conf import settings

logger = logging.getLogger(__name__)
#  Change
class Derivatives:

    @staticmethod
    def fetch_markets(base_url, token, market_place="Nasdaq OMX"):
        logger.info("Fetching market places")
        headers = {'Authorization': 'Token ' + token}
        server_url= base_url + '/api/markets/marketplaces/'
        result = requests.get(server_url,  headers=headers)
        markets=[]
        if result.status_code==200:
            for mplace in result.json():
                logger.info(mplace['name'])
                if mplace['name']==market_place:
                    logger.info("Found our main market place; list available markets traded")
                    for market_url in mplace['markets']:
                        market_url=market_url.replace("http://dev","https://dev")  # A bug on server not showing https
                        logger.info("Lookup market on URL " + str(market_url))
                        result2 = requests.get(market_url, headers=headers)
                        market=result2.json()
                        logger.info("Market traded on " + str(market_place) + ": " + str(market['name']))
                        markets.append(market['name'])
        else:
            logger.error("Problens calling EnergyDesk API " + str(result) + " " + result.text)
        return markets

    @staticmethod
    def fetch_products(base_url, token, market_place, market_name, traded_from_date):
        logger.info("Fetching products traded after date " + str(traded_from_date))
        headers = {'Authorization': 'Token ' + token}
        server_url= base_url + '/api/markets/traded_products/'
        logger.info("Fetching prices in " + market_name)
        qry_payload = {
            "market_place": market_place,
            "market_name": market_name,
            "tradingdate_from": traded_from_date,
        }

        result = requests.post(server_url, json=qry_payload, headers=headers)
        if result.status_code == 200:
            df = pd.read_json(result.json()['dataframe'], orient='records')
            logger.info("Products " + str(df))
            return df
        else:
            logger.error("Problens calling EnergyDesk API " + str(result) + " " + result.text)

    @staticmethod
    def fetch_product_prices(base_url, token, market_place, market_name, area=None):

        headers = {'Authorization': 'Token ' +token}
        server_url= base_url + '/api/markets/area_product_prices/'
        logger.info("Fetching product prices in " + market_name)
        qry_payload = {
            "market_place": market_place,
            "market_name": market_name,
            "currency_code": "EUR",
            "area": "ALL" if area is None else area
        }

        result = requests.post(server_url, json=qry_payload, headers=headers)
        if result.status_code!=200:
            logger.error("Problens calling EnergyDesk API " + str(result) + " " + result.text)
            return None
        df = pd.read_json(result.json()['dataframe'], orient='records')
        return df


    @staticmethod
    def fetch_daily_prices(base_url, token, market_place, market_name, area=None):
        headers = {'Authorization': 'Token ' + token}
        server_url= base_url + '/api/markets/area_daily_prices/'
        logger.info("Fetching daily prices in " + market_name)
        qry_payload = {
            "market_place": market_place,
            "market_name": market_name,
            "currency_code": "EUR",
            "area": "ALL" if area is None else area
        }
        result = requests.post(server_url, json=qry_payload, headers=headers)
        if result.status_code!=200:
            logger.error("Problens calling EnergyDesk API " + str(result) + " " + result.text)
            return None
        df = pd.read_json(result.json()['dataframe'], orient='records')
        return df

    @staticmethod
    def fetch_prices_for_product(base_url, token, market_place, market_name, ticker, period_from, period_until):
        logger.info("Fetching prices for product " + str(ticker))
        headers = {'Authorization': 'Token ' + token}

        server_url = base_url + '/api/markets/derivatives_prices_in_period/'
        logger.info("Fetching prices in " + market_name)
        qry_payload = {
            "market_place":market_place,
            "market_name": market_name,
            "period_from": period_from,
            "period_until": period_until,
            "currency_code": "EUR",
            "ticker": ticker
        }

        result = requests.post(server_url, json=qry_payload, headers=headers)
        if result.status_code!=200:
            logger.error("Problens calling EnergyDesk API " + str(result) + " " + result.text)
            return None
        df = pd.read_json(result.json()['dataframe'], orient='records')
        return df


