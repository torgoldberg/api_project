import json
import logging as logger
from requests import Request, Session

from main.json_data.utilities.credentials import CredentialsUtilities
from main.json_data.utilities.tenant import TenantUtilities

basic_auth = CredentialsUtilities.get_basic_auth_key_secret()
api_key = CredentialsUtilities.get_api_key()
base_url = TenantUtilities.get_tenant()


class RequestsUtilities(object):

    @staticmethod
    def assert_status_code(status_code, expected_status_code, endpoint, respond_json):
        """
        Create an assert that make sure the status code of the respond is correct
        """
        assert status_code == expected_status_code, f"Bad status code " \
                                                    f"expected: {expected_status_code} actual status " \
                                                    f"code: {status_code} " \
                                                    f"url: {base_url + endpoint}, response json: {respond_json}"
        logger.debug(f"We verified the status code")

    @staticmethod
    def json_request(request_type, endpoint, payload=None, headers={"Content-Type": "application/json"},
                     auth_type_api_key=True):
        """
        Perform the API request
        """
        auth = None
        url = base_url + endpoint
        s = Session()
        data = json.dumps(payload)
        if auth_type_api_key:
            headers["Authorization"] = f"Bearer {api_key}"
        else:
            auth = basic_auth
        request_api = Request(method=request_type, url=url, data=data, headers=headers, auth=auth)
        prepped = s.prepare_request(request_api)
        respond_api = s.send(prepped)
        logger.debug(f"{request_type} API respond: {respond_api}")

        return respond_api
