import sys
import requests
import logging
from energydeskapi.sdk.common_utils import init_api
from energydeskapi.assets.assetowners_api import AssetOwnersApi

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(message)s',
                    handlers=[logging.FileHandler("energydesk_client.log"),
                              logging.StreamHandler()])




def get_asset_owners_info(api_conn):
    df=AssetOwnersApi.get_asset_ownerships(api_conn)
    print("Asset ownerships", df)



if __name__ == '__main__':

    api_conn=init_api()
    get_asset_owners_info(api_conn)
