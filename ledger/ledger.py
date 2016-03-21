# -*- coding: utf-8 -*-
# @Author: Maxwell Amante
# @Date:   2016-03-20 13:37:09
# @Last Modified by:   max amante
# @Last Modified time: 2016-03-20 16:55:21

import logging
import os
import pkgutil
import sys

PY2 = (2, 6)
PY3 = (3, 4)
VERSION = sys.version_info

logger = logging.getLogger(__name__)


def _py3_import(mod_name, path):
    spec = importlib.util.spec_from_file_location(mod_name, path)
    mod = importlib.util.module_from_spec(spec)
    return spec.loader.exec_module(mod)


def _py2_import(mod_name, path):
    return imp.load_source(mod_name, path)


if VERSION > PY3:
    logger.debug('Using Python 3.5')
    import importlib.util
    importer = _py3_import
else:
    logger.debug('Using Python 2.7')
    import imp
    importer = _py2_import


def _service_abspath(service):
    return os.path.join(os.getcwd(), 'services', service)


def _get_services_dir():
    logger.debug('Working from: {0}'.format(os.getcwd()))
    try:
        return os.listdir(os.path.abspath('services'))
    except WindowsError:
        msg = ('Cannot find "services" directory. '
               'Ensure one exists and try again.')
        raise EnvironmentError(msg)


def _get_class_name(mod_name):
    return '{0}Service'.format(mod_name.capitalize())


class Ledger:
    @staticmethod
    def get_all_services():
        services_dir = _get_services_dir()
        svcs = {}
        logger.debug('Items in services folder:')
        for item in services_dir:
            logger.debug('Importing {0}...'.format(item))
            mod_name = item.split('.')[0]
            cls_name = _get_class_name(mod_name)
            path = _service_abspath(item)
            svcs[mod_name] = getattr(importer(mod_name, path), cls_name)()
        logger.debug('{0} services exist'.format(len(svcs)))
        return svcs

    @staticmethod
    def get_service(service):
        services = Ledger.get_all_services()
        return services[service]
