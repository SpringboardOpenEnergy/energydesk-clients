import requests
import json
import logging
import pandas as pd
logger = logging.getLogger(__name__)


class CustomerApi:
    @staticmethod
    def get_user_profile(api_connection):
        logger.info("Fetching user profile")
        json_res=api_connection.exec_get_url('/api/energydesk/getuserprofile/')
        if json_res is not None:
            return json_res
        return None