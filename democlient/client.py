import json
import os

import logging
from marketdata.derivatives import Derivatives
from marketdata.moneymarkets import MoneyMarkets
from marketdata.spotprices import SpotPrices
from marketdata.fundamentals import Fundamentals
from curvedata.forward_curves import ForwardCurves
from os.path import join, dirname
from dotenv import load_dotenv
import pytz
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
    token = os.environ.get("basic_auth_token")
    server_url = os.environ.get("server_url")
    df=Fundamentals.query_unavailable_production(server_url, token, "2022-07-01", "2022-07-05")
    #Convert to normal GMT + 1 time
    df['event_published_time'] = df['event_published_time'].apply(lambda x: convert_datetime_from_utc(x))
    df['event_start_time'] = df['event_start_time'].apply(lambda x: convert_datetime_from_utc(x))
    df['event_stop_time'] = df['event_stop_time'].apply(lambda x: convert_datetime_from_utc(x))
    print(df)
