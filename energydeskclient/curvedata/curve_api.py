import requests
import json
import logging
import pandas as pd
logger = logging.getLogger(__name__)

class CurveApi:

    # This function returns a single price (avg) for the period requested
    @staticmethod
    def get_period_price(api_connection, from_period, until_period, price_area, currency_code):
        logger.info("Fetching forward curve")
        qry_payload = {
            "price_area": price_area,
            "currency_code": currency_code,
            "period_from": from_period,
            "period_until": until_period,
        }
        json_res=api_connection.exec_post_url('/api/curvemanager/get_period_price/', qry_payload)
        if json_res is not None:
            curve_price = float(json_res['price'])
            return curve_price
        return 0


    @staticmethod
    def get_hourly_price_curve(api_connection , from_period, until_period, price_area, currency_code):
        logger.info("Fetching forward curve")
        qry_payload = {
            "price_area": price_area,
            "currency_code": currency_code,
            "period_from": from_period,
            "period_until": until_period,
        }
        json_res = api_connection.exec_post_url('/api/curvemanager/get_forward_curve/', qry_payload)

        result = requests.post(server_url, json=qry_payload,   headers=headers)
        if result.status_code==200:
            df = pd.read_json(result.json()['dataframe'], orient='records')
            logger.debug("Zero coupon rates " + str(df))
            return df
        else:
            logger.error("Problens calling EnergyDesk API " + str(result) + " " + result.text)
            return None
