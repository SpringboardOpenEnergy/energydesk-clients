import requests
import json
import logging
import pandas as pd
logger = logging.getLogger(__name__)


class CustomerApi:
    """Class for user profiles and companies

    """
    @staticmethod
    def get_user_profile(api_connection):
        """Fetches user profile

        :param api_connection: class with API token for use with API
        :type api_connection: str, required
        """
        logger.info("Fetching user profile")
        json_res=api_connection.exec_get_url('/api/energydesk/getuserprofile/')
        if json_res is not None:
            return json_res
        return None


    @staticmethod
    def get_companies(api_connection):
        """Fetches all companies

        :param api_connection: class with API token for use with API
        :type api_connection: str, required
        """
        logger.info("Fetching companylist")
        json_res=api_connection.exec_get_url('/api/customers/get_all_companies')
        if json_res is None:
            return None
        #print(json_res)
        df = pd.DataFrame(data=json_res["companies"])
        #print(df)
        #print(df.columns)
        #for index,row in df.iterrows():
        #    print(row["company_name"],row["registry_number"])
        return df

    @staticmethod
    def get_company_by_name(api_connection, company_name):
        df = CustomerApi.get_companies(api_connection)
        dfres = df.loc[df['company_name'] == company_name]
        if len(dfres.index)==0:
            logger.warning("No company named " + str(company_name))
            return None
        comppk = dfres['pk'].values[-1]
        return comppk