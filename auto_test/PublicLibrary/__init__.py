#-*- coding:utf-8 -*-
'''
    created by hch 2017-02-13
'''

from PublicLibrary.JsonDataHandle import JsonDataHandle
from PublicLibrary.ReadTestCase import read_test_case_data 
from PublicLibrary.DataPackage import data_package
from PublicLibrary.redis_db import redis_db

__version__ = '0.2'

class PublicLibrary(JsonDataHandle, read_test_case_data, data_package, redis_db):   
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
