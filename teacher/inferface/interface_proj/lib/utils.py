#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: samren
"""小工具模块，通用功能，一般与业务代码关系不大
比如，Excel读取，写入，json模块的使用，发送邮件等通用功能"""

def send_mail():
    pass


def get_strftime():
    pass


def read_excel(path):
    import xlrd
    ret_dict = {}
    data = xlrd.open_workbook(path)
    sheet = data.sheets()[0]

    nrows = sheet.nrows
    for i in range(nrows):
        if i == 0:
            continue
        ret_dict[i] = sheet.row_values(i)
        #print "第%s行是 %s" % (i, sheet.row_values(i))
    return ret_dict


if __name__ == '__main__':
    data = read_excel(r"E:\woody_laoshi\inferface\interface_proj\data\weather.xlsx")
    print type(data)
    print data.get(1)