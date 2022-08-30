import sys

import requests
import logging
from energydesk.sdk.common_utils import init_api
from energydesk.api.assets.assets_api import AssetsApi

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(message)s',
                    handlers=[logging.FileHandler("energydesk_client.log"),
                              logging.StreamHandler()])




def query_asset_info(api_conn):
    df=AssetsApi.get_asset_types(api_conn)
    print("Asset types", df)
    df=AssetsApi.get_assets_ext(api_conn)
    print("Asset list", df)


if __name__ == '__main__':

    api_conn=init_api()
    query_asset_info(api_conn)
