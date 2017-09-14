#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
import unittest
import requests
import json
import logging


class HttpBinTest(unittest.TestCase):
	u"""根据城市名获取天气预报"""
	base_url = r'http://httpbin.org'

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_with_error_key(self):
		u'''使用错误的key值发送get请求'''
		r = requests.get(self.base_url + '/ip')
		json_data = r.json()
		self.assertEqual(json_data['origin'], '112.95.135.83')


if __name__ == '__main__':
	unittest.main()