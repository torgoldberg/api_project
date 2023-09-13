import os
import logging as logger
from requests.auth import HTTPBasicAuth


class CredentialsUtilities(object):

    @staticmethod
    def get_basic_auth_key_secret():
        """
        Get the Basic AUth API credentials from the env.sh file and return it as a string
        """
        key = os.environ['BASIC_AUTH_KEY']
        secret = os.environ['BASIC_AUTH_SECRET']
        logger.debug(f"key and secret: " + key + " , " + secret)
        if not key or not secret:
            raise Exception(f"The api request credentials must be in env variables")
        else:
            key_secret = {'key': key, 'secret': secret}
        credentials = HTTPBasicAuth(key_secret['key'], key_secret['secret'])
        logger.debug(f"We successfully got the key and secret from the env variables")

        return credentials

    @staticmethod
    def get_api_key():
        """
        Get the API Key credentials from the env.sh file and return it as a string
        """
        credentials = os.environ.get("API_KEY")
        logger.debug(f"api_key: " + credentials)
        if credentials is None:
            raise Exception(f"The api request credentials must be in env variables")
        logger.debug(f"We successfully got the key from the env variables")

        return credentials

