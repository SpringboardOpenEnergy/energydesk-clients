import requests
import json
import logging
import pandas as pd
logger = logging.getLogger(__name__)

class ForwardCurves:

    # This function returns a single price (avg) for the period requested
    @staticmethod
    def get_period_price(base_url, token, from_period, until_period, price_area, currency_code):
        logger.info("Fetching spot forex rates")
        headers = {'Authorization': 'Token ' + token}
        server_url= base_url + '/api/curvemanager/get_period_price/'
        qry_payload = {
            "price_area": price_area,
            "currency_code": currency_code,
            "period_from": from_period,
            "period_until": until_period,
        }
        result = requests.post(server_url, json=qry_payload,   headers=headers)
        if result.status_code==200:
            print(result)
            json_data = result.json()
            curve_price=float(json_data['price'])
            return curve_price
        else:
            logger.error("Problens calling EnergyDesk API " + str(result) + " " + result.text)
            return None

    @staticmethod
    def get_hourly_price_curve(base_url, token, from_period, until_period, price_area, currency_code):
        logger.info("Fetching forward curve")
        headers = {'Authorization': 'Token ' +token}
        server_url=base_url + '/api/curvemanager/get_forward_curve/'
        qry_payload = {
            "price_area": price_area,
            "currency_code": currency_code,
            "period_from": from_period,
            "period_until": until_period,
        }
        result = requests.post(server_url, json=qry_payload,   headers=headers)
        if result.status_code==200:
            df = pd.read_json(result.json()['dataframe'], orient='records')
            logger.debug("Zero coupon rates " + str(df))
            return df
        else:
            logger.error("Problens calling EnergyDesk API " + str(result) + " " + result.text)
            return None
