# -*- coding: utf-8 -*-
# @Author: Maxwell Amante
# @Date:   2016-03-20 03:04:36
# @Last Modified by:   max amante
# @Last Modified time: 2016-03-20 19:31:49

import logging
logger = logging.getLogger(__name__)


class Service:
    def __init__(self):
        self.endpoints = None

    def get_endpoints(self):
        return self.endpoints

    def get_endpoint(self, endpoint):
        return self.endpoints[endpoint]
