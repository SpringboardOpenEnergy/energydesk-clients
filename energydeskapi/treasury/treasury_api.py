import requests
import json
import logging
import pandas as pd


logger = logging.getLogger(__name__)
#  Change
class TreasuryApi:
    """Description...

      """

    @staticmethod
    def get_treasury_banks(api_connection):
        logger.info("Fetching treasury bank list")
        json_res = api_connection.exec_get_url('/api/treasury/treasurybanks/')
        print(json_res)
        if json_res is None:
            return None
        df = pd.DataFrame(data=json_res)
        return df

