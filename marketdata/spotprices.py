import requests
import json
import logging
import pandas as pd
logger = logging.getLogger(__name__)

class SpotPrices:


    @staticmethod
    def fetch_spot_prices(base_url, token, market_place, period_from, period_until):
        logger.info("Fetching spot prices")
        headers = {'Authorization': 'Token ' + token}
        server_url = base_url + '/api/markets/spot_prices_in_period/'

        qry_payload = {
            "market_place": market_place,
            "period_from": period_from,
            "period_until": period_until,
            "currency_code": "NOK",
            "market_name": "NOK",
        }


        result = requests.post(server_url, json=qry_payload, headers=headers)
        if result.status_code!=200:
            logger.error("Problens calling EnergyDesk API " + str(result) + " " + result.text)
            return None
        df = pd.read_json(result.json()['dataframe'], orient='records')
        return df


