import requests
import json
import logging
import pandas as pd
logger = logging.getLogger(__name__)

class AssetsApi:
    """ Class for assets

    """

    # This function returns a single price (avg) for the period requested
    @staticmethod
    def register_assets(api_connection, asset_list):
        """ Registers assets

        :param api_connection: class with API token for use with API
        :type api_connection: str, required
        :param asset_list: list of assets
        :type asset_list: str, required
        """
        logger.info("Registering " + str(len(asset_list) )+ " assets")
        for asset in asset_list:
            json_res=api_connection.exec_post_url('/api/assets/asset/', asset)


    @staticmethod
    def get_asset_types(api_connection):
        """ Receives the type of assets

        :param api_connection: class with API token for use with API
        :type api_connection: str, required
        """
        json_res = api_connection.exec_get_url('/api/assets/assettype/')
        if json_res is None:
            return None
        print(json_res)
        df = pd.DataFrame(data=json_res)
        return df
