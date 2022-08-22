import requests
import json
import logging
import pandas as pd
logger = logging.getLogger(__name__)

class AssetOwnersApi:

    # Create a json file from NetworkX DiGraph defining ownerships
    @staticmethod
    def save_ownerships(api_connection, ownership_graph_json):
       json_res=api_connection.exec_post_url('/api/asset-ownership/save-ownership-graph/', ownership_graph_json)


    @staticmethod
    def load_ownerships(api_connection):
        json_res = api_connection.exec_get_url('/api/asset-ownership/load-ownership-graph/')
        if json_res is None:
            return None
        print(json_res)
        df = pd.DataFrame(data=json_res)
        return df