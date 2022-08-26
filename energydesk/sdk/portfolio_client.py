
import environ
import logging
from energydesk.sdk.api_connection import ApiConnection
from energydesk.api.portfolios.tradingbooks_api import TradingBooksApi
from energydesk.api.portfolios.contracts_api import ContractsApi, Contract
from os.path import join, dirname
from moneyed import Money, NOK, EUR
from energydesk.sdk.datetime_utils import convert_datime_to_utcstr, convert_datime_to_locstr
from dotenv import load_dotenv
from moneyed.l10n import format_money
from dateutil import parser, relativedelta
from datetime import datetime, timedelta
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(message)s',
                    handlers=[logging.FileHandler("energydesk_client.log"),
                              logging.StreamHandler()])

def load_env():
    """ Loads environment file

    """
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


    class PrintableMoney(Money):
        def __str__(self):
            return format_money(self, locale='en_DE')


    yester = (datetime.today() + timedelta(days=-1)).replace( hour=0, minute=0, second=0, microsecond=0)
    dtstr1=convert_datime_to_utcstr(yester)
    dtstr2=convert_datime_to_locstr(yester, "Europe/Oslo")  #In order to get the date correct
    trading_book=TradingBooksApi.load_tradingbook_by_pk(api_conn, 2)
    c=Contract("EXT ID 238231", trading_book, PrintableMoney(45, NOK),
                                    PrintableMoney(2, EUR),
                                    PrintableMoney(2, EUR),
               dtstr2[0:10],dtstr1)
    ContractsApi.register_contract(api_conn,[c])