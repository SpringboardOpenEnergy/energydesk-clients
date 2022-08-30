import sys

import requests
import logging
from energydesk.sdk.common_utils import init_api
from energydesk.api.customers.customer_api import CustomerApi

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(message)s',
                    handlers=[logging.FileHandler("energydesk_client.log"),
                              logging.StreamHandler()])


def query_companies(api_conn):
    json_companies=CustomerApi.get_companies(api_conn)
    all_companies_df=CustomerApi.get_companies_ext_df(api_conn)
    print(all_companies_df)

def query_company_types(api_conn):
    df=CustomerApi.get_company_types_df(api_conn)
    print(df)

def list_users(api_conn):
    df=CustomerApi.get_users(api_conn)
    print(df)

if __name__ == '__main__':

    api_conn=init_api()
    user_profile=CustomerApi.get_user_profile(api_conn)
    print(user_profile)
    list_users(api_conn)
