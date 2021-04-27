# coding=utf-8

#
# Wi-Fi simple geolocation tool
# Copyright (c) 2015 - 2019 EasyCoding Team
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import os

from ..linux import FetcherLinux
from ..windows import FetcherWindows


class FetcherFactory:
    """
    Static class with factory methods.
    """

    @staticmethod
    def create():
        """
        Get the correct instance of the fetcher. Factory method.
        :return: An instance of the desired class.
        :rtype: Any
        """
        return FetcherLinux() if os.name == 'posix' else FetcherWindows()
