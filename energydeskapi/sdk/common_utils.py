import json
import logging
from os.path import join, dirname
from dotenv import load_dotenv
import pytz, environ
from energydeskapi.sdk.api_connection import ApiConnection
logger = logging.getLogger(__name__)

def load_env():
    """ Loads environment file
    """
    logging.info("Loading environment")
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)


def init_api():
    load_env()
    env = environ.Env()
    tok = env.str('basic_auth_token')
    url= env.str('server_url')
    api_conn=ApiConnection(url)
    api_conn.set_token(tok, "Token")
    return api_conn