import requests
import json
import logging
import pandas as pd
from energydesk.sdk.money_utils import gen_json_money
from energydesk.api.portfolios.tradingbooks_api import TradingBooksApi
from moneyed.l10n import format_money
from energydesk.sdk.datetime_utils import convert_datime_to_utcstr
from datetime import datetime
logger = logging.getLogger(__name__)
#  Change
class Contract:
    def __init__(self,
                 external_contract_id,
                 trading_book,
                 price,
                 trading_fee,
                 clearing_fee,
                 trade_date,
                 trade_datetime
                 ):
        self.external_contract_id=external_contract_id
        self.trading_book=trading_book
        self.price=price
        self.trading_fee=trading_fee
        self.clearing_fee=clearing_fee
        self.trade_date=trade_date
        self.trade_datetime=trade_datetime


class ContractsApi:
    """Description...

      """

    @staticmethod
    def register_contract(api_connection,
                          contracts):
        logger.info("Registering contract")
        #print(format_money(price, locale='en_DE'))
        json_records=[]
        for contract in contracts:

            #trbook=TradingBooksApi.load_tradingbook_by_pk(api_connection, contract.trading_book)
            contract_record={"pk":0,
                   "external_contract_id":contract.external_contract_id,
                   "trading_book": contract.trading_book,
                   "trade_date": contract.trade_date,
                   "trade_time": contract.trade_datetime,
                   "registration_time":convert_datime_to_utcstr(datetime.now()),
                   "price": gen_json_money(contract.price),
                   "trading_fee": gen_json_money(contract.trading_fee),
                   "clearing_fee": gen_json_money(contract.clearing_fee)}
            print(contract_record)
            json_records.append(contract_record)


        json_res=api_connection.exec_post_url('/api/portfoliomanager/register_contracts/',json_records)
        #print(json_res)

    @staticmethod
    def load_tradingbook_by_pk(api_connection, pk):
        logger.info("Fetching trading books")
        json_res = api_connection.exec_get_url('/api/portfoliomanager/tradingbook/')
        for r in json_res:
            if r['pk']==pk:
                return r
        return None