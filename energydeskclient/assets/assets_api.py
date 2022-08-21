import requests
import json
import logging
import pandas as pd
logger = logging.getLogger(__name__)

class AssetsApi:

    # This function returns a single price (avg) for the period requested
    @staticmethod
    def register_assets(api_connection, asset_list):
        logger.info("Registering " + str(len(asset_list) )+ " assets")
        for asset in asset_list:
            json_res=api_connection.exec_post_url('/api/assets/asset/', asset)


    @staticmethod
    def get_asset_types(api_connection):
        json_res = api_connection.exec_get_url('/api/assets/assettype/')
        if json_res is None:
            return None
        print(json_res)
        df = pd.DataFrame(data=json_res)
        return df
