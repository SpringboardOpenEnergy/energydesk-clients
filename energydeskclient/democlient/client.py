import sys

import requests
import logging
from energydeskclient.api.api_connection import ApiConnection
from energydeskclient.curvedata.curve_api import CurveApi
from energydeskclient.marketdata.derivatives_api import DerivativesApi
from energydeskclient.customer.customer_api import CustomerApi
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
    timezone = pytz.timezone(loczone)
    utc_dt=parser.isoparse(str(utc_str))
    d_loc = utc_dt.astimezone(timezone)
    return d_loc

def load_env():
    logging.info("Loading environment")
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)

if __name__ == '__main__':
    load_env()
    env = environ.Env()
    tok = env.str('basic_auth_token')
    url= env.str('server_url')
    api_conn=ApiConnection("","",url)
    api_conn.set_token(tok, "Token")

    #price=CurveApi.get_period_price(api_conn, "2023-01-01", "2023-04-01","NO1", "EUR")
    #print(price)
    user_profile=CustomerApi.get_user_profile(api_conn)
    print(user_profile)
    DerivativesApi.fetch_markets(api_conn)
    DerivativesApi.fetch_products(api_conn, "Nasdaq OMX", "Nordic Power", "2022-01-01")
