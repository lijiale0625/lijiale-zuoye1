# -*- coding: utf-8 -*-
#!/usr/bin/env python   
# author: lijiale
"""小工具模块，通用模块，一般与业务代码关系不大
比如Excel读取，写入，json模块的使用，发送邮件等通用功能"""
import  os
def send_mail():
    pass

def get_strftime():
    pass

def read_excel(path):
    import xlrd
    ret_dict = {}
    data = xlrd.open_workbook(path)
    sheet = data.sheets()[0]
    # print sheet.nrows
    # print sheet.ncols
    nrows = sheet.nrows
    for i in range(nrows):
        if i == 0:
            continue
        ret_dict[i] = sheet.row_values(i)
    #print ret_dict
        #print u"第%s行是%s" % (i,sheet.row_values(i))
    return ret_dict

    #return {1:[],2：[]，3}：[]

if __name__ == '__main__':
    read_excel("E:\woody\lijiale-zuoye1\myproj\data\login_account.xlsx")


