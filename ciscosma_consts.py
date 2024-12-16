# File: ciscosma_consts.py
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

# Cisco SMA Constants

CISCOSMA_VALID_ORDER_BY = ["from_address", "to_address", "subject"]
CISCOSMA_VALID_ORDER_DIRECTIONS = ["asc", "desc"]
CISCOSMA_VALID_FILTER_OPERATORS = ["contains", "is", "begins_with", "ends_with", "does_not_contain"]

CISCOSMA_GET_TOKEN_ENDPOINT = "/sma/api/v2.0/login"
CISCOSMA_GET_MESSAGE_DETAILS_ENDPOINT = "/sma/api/v2.0/quarantine/messages/details"
CISCOSMA_GET_MESSAGE_TRACKING_DETAILS_ENDPOINT = "/sma/api/v2.0/message-tracking/details"
CISCOSMA_SEARCH_MESSAGES_ENDPOINT = "/sma/api/v2.0/quarantine/messages"
CISCOSMA_SEARCH_TRACKING_MESSAGES_ENDPOINT = "/sma/api/v2.0/message-tracking/messages"

# Future endpoints
# GET /api/v2.0/reporting/report?resource_attribute
# GET /api/v2.0/reporting/report/counter?resource_attribute

# GET/sma/api/v2.0/message-tracking/messages?resource_attribute

# GET /api/v2.0/quarantine/messages?resource_attribute
# GET /api/v2.0/quarantine/messages?resource_attribute(search)
# GET /api/v2.0/quarantine/messages?resource_attribute(download attachment -> possible)
# POST /api/v2.0/quarantine/messages?resource_attribute (release)

# POST /api/v2.0/quarantine/safelist?resource_attribute
# POST /api/v2.0/quarantine/blocklist?resource_attribute

# DELETE /api/v2.0/quarantine/safelist?resource_attribute
# DELETE /api/v2.0/quarantine/blocklist?resource_attribute
