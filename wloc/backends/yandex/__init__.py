# coding=utf-8

# SPDX-FileCopyrightText: 2015-2021 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later

import json
import requests

from ...backends import BackendCommon
from ...exception import BackendError


class BackendYandex(BackendCommon):
    """
    Class for working with Yandex Locator API.
    """

    def _execute(self, netlist) -> list:
        """
        Internal implementation of Yandex-like geolocation API fetcher.
        :param netlist: The list of available Wi-Fi networks.
        :exception BackendError Raises on HTTP errors.
        :return: Coordinates (float).
        """
        # Generating base JSON structure...
        jdata = {'common': {'version': '1.0', 'api_key': self._apikey}, 'wifi_networks': []}

        # Retrieving available networks...
        for arr in netlist:
            jdata['wifi_networks'].append({'mac': arr[0], 'signal_strength': arr[1], 'age': 0})

        # Sending our JSON to API...
        r = requests.post(self._uri, data={'json': json.dumps(jdata)}, headers={'content-type': 'application/json'})

        # Checking return code...
        if r.status_code != 200:
            raise BackendError('Server returned code: %s. Text message: %s' % (r.status_code, r.text))

        # Parsing JSON response...
        result = json.loads(r.content)

        # Returning result...
        return [float(result['position']['latitude']), float(result['position']['longitude'])]

    @property
    def _uri(self) -> str:
        """
        Gets fully-qualified geolocation API URI.
        :return: Fully-qualified geolocation API URI.
        """
        return self._endpoint

    def __init__(self, apikey: str):
        """
        Main constructor of the BackendYandex class.
        :param apikey: String with the API token (key).
        """
        super().__init__(apikey)
        self._endpoint: str = 'https://api.lbs.yandex.net/geolocation'