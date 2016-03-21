# -*- coding: utf-8 -*-
# @Author: Maxwell Amante
# @Date:   2016-03-20 18:40:06
# @Last Modified by:   max amante
# @Last Modified time: 2016-03-20 19:52:44

import logging
logger = logging.getLogger(__name__)


class Endpoint:
    def __init__(self):
        logger.debug('endpoint created')

    def create(self):
        logger.debug('create invoked')
        return 'create result'

    def list(self):
        logger.debug('list invoked')
        return 'list result'

    def get(self):
        logger.debug('get invoked')
        return 'get result'

    def update(self):
        logger.debug('update invoked')
        return 'update result'

    def delete(self):
        logger.debug('delete invoked')
        return 'delete result'
