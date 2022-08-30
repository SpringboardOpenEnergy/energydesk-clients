import sys

import requests
import logging
from energydesk.sdk.api_connection import ApiConnection
from energydesk.api.contracts.contracts_api import ContractsApi

from energydesk.sdk.common_utils import init_api
import pytz, environ
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(message)s',
                    handlers=[logging.FileHandler("energydesk_client.log"),
                              logging.StreamHandler()])


def get_contract_types(api_conn):
    df=ContractsApi.list_commodity_types(api_conn)
    print(df)
    df=ContractsApi.list_instrument_types(api_conn)
    print(df)
    df=ContractsApi.list_contract_types(api_conn)
    print(df)
    df=ContractsApi.list_contract_statuses(api_conn)
    print(df)

if __name__ == '__main__':
    api_conn=init_api()
    get_contract_types(api_conn)
