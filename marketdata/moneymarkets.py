import requests
import json
import logging
import pandas as pd
logger = logging.getLogger(__name__)

class MoneyMarkets:

    @staticmethod
    def fetch_forex_spot_rates(base_url, token):
        logger.info("Fetching spot forex rates")
        headers = {'Authorization': 'Token ' + token}
        server_url= base_url + '/api/moneymarkets/spot_forex_rates/'
        qry_payload = {
            "period_from": "2019-01-01",
            "period_until": "2022-06-01",
        }
        result = requests.post(server_url, json=qry_payload,   headers=headers)
        if result.status_code==200:
            df = pd.read_json(result.json()['dataframe'], orient='records')
            logger.debug("Forex " + str(df))
            return df
        else:
            logger.error("Problens calling EnergyDesk API " + str(result) + " " + result.text)
            return None

    @staticmethod
    def fetch_zero_coupon_rates(base_url, token):
        logger.info("Fetching zero coupon rates")
        headers = {'Authorization': 'Token ' +token}
        server_url=base_url + '/api/moneymarkets/zero_coupon_rates/'
        qry_payload = {
            "period_from": "2019-01-01",
            "period_until": "2022-06-01",
        }
        result = requests.post(server_url, json=qry_payload,   headers=headers)
        if result.status_code==200:
            df = pd.read_json(result.json()['dataframe'], orient='records')
            logger.debug("Zero coupon rates " + str(df))
            return df
        else:
            logger.error("Problens calling EnergyDesk API " + str(result) + " " + result.text)
            return None
