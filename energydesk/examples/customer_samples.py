import sys

import requests
import logging
from energydesk.sdk.api_connection import ApiConnection
from energydesk.api.customers.customer_api import CustomerApi

from os.path import join, dirname
from dotenv import load_dotenv
import pytz, environ
from dateutil import parser
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(message)s',
                    handlers=[logging.FileHandler("energydesk_client.log"),
                              logging.StreamHandler()])

# Data retrieved from server are in UTC time ("GMT without daylight savings time")
# This function converts to local time
def convert_datetime_from_utc(utc_str, loczone="Europe/Oslo"):
    """ Converts datetime from UTC

    :param utc_str: string of UTC
    :type utc_str: str, required
    :param loczone: specified location
    :type loczone: str, required
    """
    timezone = pytz.timezone(loczone)
    utc_dt=parser.isoparse(str(utc_str))
    d_loc = utc_dt.astimezone(timezone)
    return d_loc

def load_env():
    """ Loads environment file

    """
    logging.info("Loading environment")
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)

def query_companies(api_conn):
    json_companies=CustomerApi.get_companies(api_conn)
    all_companies_df=CustomerApi.get_companies_ext_df(api_conn)
    print(all_companies_df)

def query_company_types(api_conn):
    df=CustomerApi.get_company_types_df(api_conn)
    print(df)



if __name__ == '__main__':
    load_env()
    env = environ.Env()
    tok = env.str('basic_auth_token')
    url= env.str('server_url')
    api_conn=ApiConnection("","",url)
    api_conn.set_token(tok, "Token")

    user_profile=CustomerApi.get_user_profile(api_conn)
    query_company_types(api_conn)