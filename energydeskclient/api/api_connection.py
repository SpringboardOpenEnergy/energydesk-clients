import requests
import http.client
import json
import logging
logger = logging.getLogger(__name__)

class ApiConnection:

    def __init__(self, customer, platform="test", override_baseurl=None):
        self.base_url=override_baseurl if override_baseurl is not None else "https://" + platform + "-api." + customer + ".energydesk.no"
        self.set_token("", "Token")

    def get_base_url(self):
        return self.base_url

    def validate_token(self, token):
        http.client._MAXHEADERS = 1000
        server_url = self.get_base_url() + "/auth/convert-token"
        payload = {
            "grant_type": "convert_token",
            "client_id": "client_id",
            "client_secret": "client_secret",
            "backend": "google-oauth2",
            "token": token}
        result = requests.post(server_url, json=payload)
        if result.status_code != 200:
            print("Could not validate user with backend")
            return False
        access_token = result.json()['access_token']
        self.set_token(access_token, "Bearer")
        return True

    def set_token(self, token, token_type="Bearer"):
        self.token_type=token_type
        self.token=token

    def get_authorization_header(self):
        return {'Authorization':  self.token_type + ' ' + self.token}

    def exec_post_url(self, trailing_url, payload, extra_headers={}):
        headers=self.get_authorization_header()
        for key in extra_headers:
            headers[key]=extra_headers[key]
        server_url= self.get_base_url() + trailing_url
        logger.info("Calling URL " + str(server_url))
        logger.info("...with payload " + str(payload) + " and headers " + str(headers))
        result = requests.post(server_url, json=payload,   headers=headers)
        if result.status_code<202:
            json_data = result.json()
            return json_data
        else:
            logger.error("Problens calling EnergyDesk API " + str(result) + " " + result.text)
            return None

    def exec_get_url(self, trailing_url,  extra_headers={}):
        headers=self.get_authorization_header()
        for key in extra_headers:
            headers[key]=extra_headers[key]
        server_url= self.get_base_url() + trailing_url
        logger.info("Calling URL " + str(server_url))
        #logger.info("...with payload " + str(payload) + " and headers " + str(headers))
        result = requests.get(server_url,  headers=headers)
        if result.status_code<202:
            json_data = result.json()
            return json_data
        else:
            logger.error("Problens calling EnergyDesk API " + str(result) + " " + result.text)
            return None