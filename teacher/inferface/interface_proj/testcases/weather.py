#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
import unittest
import requests
import json
import logging
from lib.utils import  *

#from config import *

class WeatherTest(unittest.TestCase):
	u"""根据城市名获取天气预报"""
	base_url = r'http://v.juhe.cn/weather/index'

	def setUp(self):
		pass

	def tearDown(self):
		pass
	def test_with_validkey_by_cityname(self):
		u'''正确的key正确城市'''
		self.data_dict = read_excel("E:\woody_laoshi\inferface\interface_proj\data\weather.xlsx")
		key, cityname, dtype,format,resultcode,error_code,reason = self.data_dict[1]
		print(self.data_dict[1])
		params={'key': key, 'cityname': cityname}
		print params
		r = requests.get(self.base_url, params=params)
		json_data = r.json()
		self.assertEqual(json_data['resultcode'], resultcode)
		self.assertEqual(json_data['error_code'], error_code)
		if json_data['error_code'] == error_code:
			logging.info(reason)
	def test_with_nullkey_by_cityname(self):
		u'''null的key正确城市'''
		self.data_dict = read_excel("E:\woody_laoshi\inferface\interface_proj\data\weather.xlsx")
		key, cityname, dtype,format,resultcode,error_code,reason = self.data_dict[2]
		print(self.data_dict[2])
		params={'key': key, 'cityname': cityname}
		print params
		r = requests.get(self.base_url, params=params)
		json_data = r.json()
		self.assertEqual(json_data['resultcode'], resultcode)
		self.assertEqual(json_data['error_code'], error_code)
		if json_data['error_code'] == error_code:
			logging.info(reason)
	def test_with_errorkey_by_cityname(self):
		u'''错误的key正确城市'''
		self.data_dict = read_excel("E:\woody_laoshi\inferface\interface_proj\data\weather.xlsx")
		key, cityname, dtype,format,resultcode,error_code,reason = self.data_dict[3]
		print(self.data_dict[3])
		params={'key': key, 'cityname': cityname}
		print params
		r = requests.get(self.base_url, params=params)
		json_data = r.json()
		self.assertEqual(json_data['resultcode'], resultcode)
		self.assertEqual(json_data['error_code'], error_code)
		if json_data['error_code'] == error_code:
			logging.info(reason)
	def test_with_validkey_by_nullcityname(self):
		u'''正确的key，null的城市'''
		self.data_dict = read_excel("E:\woody_laoshi\inferface\interface_proj\data\weather.xlsx")
		key, cityname, dtype,format,resultcode,error_code,reason = self.data_dict[4]
		print(self.data_dict[4])
		params={'key': key, 'cityname': cityname}
		print params
		r = requests.get(self.base_url, params=params)
		json_data = r.json()
		self.assertEqual(json_data['resultcode'], resultcode)
		self.assertEqual(json_data['error_code'], error_code)
		if json_data['error_code'] == error_code:
			logging.info(reason)
	def test_with_validkey_by_errorcityname(self):
		u'''正确的key，error的城市'''
		self.data_dict = read_excel("E:\woody_laoshi\inferface\interface_proj\data\weather.xlsx")
		key, cityname, dtype,format,resultcode,error_code,reason = self.data_dict[5]
		print(self.data_dict[5])
		params={'key': key, 'cityname': cityname}
		print params
		r = requests.get(self.base_url, params=params)
		json_data = r.json()
		self.assertEqual(json_data['resultcode'], resultcode)
		self.assertEqual(json_data['error_code'], error_code)
		if json_data['error_code'] == error_code:
			logging.info(reason)
	def test_with_validkey_by_cityname_with_dtypy_json(self):
		u'''正确的key，error的城市'''
		self.data_dict = read_excel("E:\woody_laoshi\inferface\interface_proj\data\weather.xlsx")
		key, cityname, dtype,format,resultcode,error_code,reason = self.data_dict[6]
		print(self.data_dict[6])
		params={'key': key, 'cityname': cityname}
		print params
		r = requests.get(self.base_url, params=params)
		json_data = r.json()
		self.assertEqual(json_data['resultcode'], resultcode)
		self.assertEqual(json_data['error_code'], error_code)
		if json_data['error_code'] == error_code:
			logging.info(reason)
	def test_with_validkey_by_cityname_with_dtypy_xml(self):
		u'''正确的key，error的城市'''
		self.data_dict = read_excel("E:\woody_laoshi\inferface\interface_proj\data\weather.xlsx")
		key, cityname, dtype,format,resultcode,error_code,reason = self.data_dict[7]
		print(self.data_dict[7])
		params={'key': key, 'cityname': cityname}
		print params
		r = requests.get(self.base_url, params=params)
		json_data = r.json()
		self.assertEqual(json_data['resultcode'], resultcode)
		self.assertEqual(json_data['error_code'], error_code)
		if json_data['error_code'] == error_code:
			logging.info(reason)
	def test_with_validkey_by_cityname_with_format_1(self):
		u'''正确的key，error的城市'''
		self.data_dict = read_excel("E:\woody_laoshi\inferface\interface_proj\data\weather.xlsx")
		key, cityname, dtype,format,resultcode,error_code,reason = self.data_dict[8]
		print(self.data_dict[8])
		params={'key': key, 'cityname': cityname}
		print params
		r = requests.get(self.base_url, params=params)
		json_data = r.json()
		self.assertEqual(json_data['resultcode'], resultcode)
		self.assertEqual(json_data['error_code'], error_code)
		if json_data['error_code'] == error_code:
			logging.info(reason)
	def test_with_validkey_by_cityname_with_format_2(self):
		u'''正确的key，error的城市'''
		self.data_dict = read_excel("E:\woody_laoshi\inferface\interface_proj\data\weather.xlsx")
		key, cityname, dtype,format,resultcode,error_code,reason = self.data_dict[9]
		print(self.data_dict[9])
		params={'key': key, 'cityname': cityname}
		print params
		r = requests.get(self.base_url, params=params)
		json_data = r.json()
		self.assertEqual(json_data['resultcode'], resultcode)
		self.assertEqual(json_data['error_code'], error_code)
		if json_data['error_code'] == error_code:
			logging.info(reason)
	# def test_with_error_key(self):
	# 	u'''使用错误的key值发送get请求'''
	# 	r = requests.get(self.base_url)
	# 	json_data = r.json()
	# 	self.assertEqual(json_data['resultcode'], '101')
	# 	self.assertEqual(json_data['error_code'], 10001)
	# 	self.assertEqual(json_data['reason'], u'错误的请求KEY!')
	# 	if json_data['error_code'] == 10001:
	# 		logging.info(u"错误的请求KEY")

	# def test_with_null_key(self):
	# 	u'''key为null'''
	# 	params={'key': '', 'cityname': '深圳'}
	# 	print params
	# 	r = requests.get(self.base_url, params=params)
	# 	json_data = r.json()
	# 	print json_data
	# 	print json_data['error_code']
	# 	m = self.assertEqual(json_data['resultcode'], '101')
	# 	self.assertEqual(json_data['error_code'], 10001)
	# 	if json_data['error_code'] == 10001:
	# 		logging.info(u"错误的请求KEY")
	# def test_with_error_key1(self):
	# 	u'''错误的key'''
	# 	params={'key': '7160d5156d63176bf48ba18b88d4ab0fx', 'cityname': '深圳'}
	# 	print params
	# 	r = requests.get(self.base_url, params=params)
	# 	json_data = r.json()
	# 	print json_data
	# 	print json_data['error_code']
	# 	if json_data['error_code'] == 10001:
	# 		logging.info(u"错误的请求KEY")
	# def test_with_key(self):
	# 	u'''正确的key'''
	# 	params={'key': '7160d5156d63176bf48ba18b88d4ab0f', 'cityname': '深圳'}
	# 	print params
	# 	r = requests.get(self.base_url, params=params)
	# 	json_data = r.json()
	# 	print json_data
	# 	print json_data['error_code']
	# 	if json_data['error_code'] != 10001:
	# 		logging.info(u"不是错误的请求KEY")
	# def test_get_weather_by_nullcityname(self):
	# 	u'''正确的key城市为空'''
	# 	params={'key': '7160d5156d63176bf48ba18b88d4ab0f', 'cityname': ''}
	# 	print params
	# 	r = requests.get(self.base_url, params=params)
	# 	json_data = r.json()
	# 	print json_data
	# 	print json_data['error_code']
	# 	if json_data['error_code'] == 203901:
	# 		logging.info(u"Error Cityname!")
	# def test_get_weather_by_errorcityname(self):
	# 	u'''正确的key城市错误'''
	# 	params={'key': '7160d5156d63176bf48ba18b88d4ab0f', 'cityname': '深圳1'}
	# 	print params
	# 	r = requests.get(self.base_url, params=params)
	# 	json_data = r.json()
	# 	print json_data
	# 	print json_data['error_code']
	# 	if json_data['error_code'] == 203902:
	# 		logging.info(u"查询不到该城市的信息")



if __name__ == '__main__':
	unittest.main()