# File: ciscosma_connector.py
#
# Copyright (c) 2019-2024 Splunk Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions
# and limitations under the License.

# Cisco SMA Connector

import base64

import phantom.app as phantom
import requests
from phantom.action_result import ActionResult
from phantom.base_connector import BaseConnector

from ciscosma_consts import CISCOSMA_GET_TOKEN_ENDPOINT


class CiscoSmaConnector(BaseConnector):
    def __init__(self):
        super(CiscoSmaConnector, self).__init__()
        self._base_url = None
        self._username = None
        self._password = None
        self._verify = False
        self._jwt_token = None

    def _make_rest_call(self, endpoint, action_result, headers=None, params=None, data=None, json=None, method="get"):
        """Function that makes the REST call to the app.

        :param endpoint: REST endpoint that needs to be appended to the service address
        :param action_result: object of ActionResult class
        :param headers: request headers
        :param params: request parameters
        :param data: request body
        :param json: JSON object
        :param method: GET/POST/PUT/DELETE/PATCH (Default will be GET)
        :return: status phantom.APP_ERROR/phantom.APP_SUCCESS(along with appropriate message),
        response obtained by making an API call
        """
        resp_json = None

        try:
            kwargs = {"json": json, "data": data, "headers": headers, "params": params, "verify": self._verify}

            response = requests.request(method, endpoint, **kwargs)

            try:
                resp_json = response.json()
            except ValueError:
                return action_result.set_status(phantom.APP_ERROR, f"Invalid JSON response from server: {response.text}"), None

            if response.status_code != 200:
                return (
                    action_result.set_status(
                        phantom.APP_ERROR, f"API call failed. Status code: {response.status_code}. Response: {response.text}"
                    ),
                    None,
                )

            return phantom.APP_SUCCESS, resp_json

        except requests.exceptions.RequestException as e:
            return action_result.set_status(phantom.APP_ERROR, f"Error connecting to server: {str(e)}"), None
        except Exception as e:
            return action_result.set_status(phantom.APP_ERROR, f"Error making REST call: {str(e)}"), None

    def _make_authenticated_request(self, action_result, endpoint, headers=None, params=None, data=None, json_data=None, method="get"):
        """Function that makes authenticated REST calls to the app with automatic token refresh.

        :param endpoint: REST endpoint that needs to be appended to the service address
        :param action_result: object of ActionResult class
        :param headers: request headers
        :param params: request parameters
        :param data: request body
        :param json_data: JSON object
        :param method: GET/POST/PUT/DELETE/PATCH (Default will be GET)
        :return: status phantom.APP_ERROR/phantom.APP_SUCCESS(along with appropriate message),
        response obtained by making an API call
        """
        url = f"{self._base_url}{endpoint}"
        if headers is None:
            headers = {"Content-Type": "application/json", "Accept": "application/json"}

        # Get Token
        if not self._jwt_token:
            ret_val, token = self._get_jwt_token(action_result)
            if phantom.is_fail(ret_val):
                return phantom.APP_ERROR, None
            self._jwt_token = token

        headers.update({"Authorization": f"Bearer {self._jwt_token}"})

        ret_val, resp_json = self._make_rest_call(url, action_result, headers, params, data, json_data, method)

        # Generate new token if expired
        if ret_val == phantom.APP_ERROR and "token" in action_result.get_message().lower():
            ret_val, token = self._get_jwt_token(action_result)
            if phantom.is_fail(ret_val):
                return action_result.get_status(), None

            self._jwt_token = token
            headers.update({"Authorization": f"Bearer {self._jwt_token}"})

            ret_val, resp_json = self._make_rest_call(url, action_result, headers, params, data, json_data, method)

        if phantom.is_fail(ret_val):
            return action_result.get_status(), None

        return phantom.APP_SUCCESS, resp_json

    def _get_jwt_token(self, action_result):
        payload = {
            "data": {
                "userName": base64.b64encode(self._username.encode()).decode(),
                "passphrase": base64.b64encode(self._password.encode()).decode(),
            }
        }

        ret_val, resp_json = self._make_rest_call(f"{self._base_url}{CISCOSMA_GET_TOKEN_ENDPOINT}", action_result, json=payload, method="post")

        if phantom.is_fail(ret_val):
            return ret_val, None

        if not (jwt_token := resp_json.get("data", {}).get("jwtToken")):
            return action_result.set_status(phantom.APP_ERROR, "JWT token not found in response"), None

        return phantom.APP_SUCCESS, jwt_token

    def _handle_test_connectivity(self, param):
        action_result = self.add_action_result(ActionResult(dict(param)))

        self.save_progress("Connecting to Cisco SMA...")
        ret_val, _ = self._make_authenticated_request(action_result, CISCOSMA_GET_TOKEN_ENDPOINT, method="post")

        if phantom.is_fail(ret_val):
            self.save_progress("Test Connectivity Failed")
            return action_result.get_status()

        self.save_progress("Test Connectivity Passed")
        return action_result.set_status(phantom.APP_SUCCESS)

    def initialize(self):
        config = self.get_config()
        self._base_url = config["host"].rstrip("/")
        self._username = config["username"]
        self._password = config["password"]
        self._verify = config.get("verify_server_cert", False)
        return phantom.APP_SUCCESS

    def handle_action(self, param):
        action = self.get_action_identifier()
        if action == "test_connectivity":
            return self._handle_test_connectivity(param)
        return phantom.APP_ERROR


if __name__ == "__main__":
    import sys

    import pudb

    pudb.set_trace()

    connector = CiscoSmaConnector()
    connector.print_progress_message = True

    sys.exit(0)
