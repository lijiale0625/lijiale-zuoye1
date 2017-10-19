#!/usr/bin/python
# -*- coding: UTF-8 -*-
import  urllib2,urllib,requests
#
# r = urllib2.Request(url='http://172.30.0.227:18008/obs/Terminal/bindSN')
# r.add_header('Content-Type', 'application/json')
# r.add_data(urllib.urlencode({"cId":"1005","boxSN":"018399998007","merchantId":20009560,"operatorId":20043115}))
# response = urllib2.urlopen(r)  # post method

import urllib #sohu 手机主页
# url = 'http://m.sohu.com/?v=3&_once_=000025_v2tov3&_smuid=\ ICvXXapq5EfTpQTVq6Tpz'
# resp = urllib.urlopen(url)
# page = resp.read()
# f = open('./urllib_index.html', 'w')
# f.write(page)
# print dir(resp)
# print resp.getcode(), resp.geturl(), resp.info(), resp.headers, resp.url

# url = 'http://m.sohu.com/?v=3&_once_=000025_v2tov3&_smuid\
# =ICvXXapq5EfTpQTVq6Tpz'
# req = urllib2.Request(url)
# resp = urllib2.urlopen(req)
# page = resp.read()

# import urllib
# import urllib2
# url = 'http://www.someserver.com/cgi-bin/register.cgi'
# values = {'name' : 'Michael Foord',
#    'location' : 'Northampton',
#    'language' : 'Python' }
# data = urllib.urlencode(values)
# req = urllib2.Request(url, data)   #send post
# response = urllib2.urlopen(req)
# page = response.read()

