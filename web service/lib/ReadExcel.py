#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: lijiale
#! encoding=utf-8
import xlrd
#import xlwt
import xml.dom.minidom
import os,sys

class OpExcel():
    table = ''
    tabledata = []
    def __init__(self,path,sheet):
        try:
            data = xlrd.open_workbook(path)
        except Exception, e:
            print str(e)
            sys.exit()
        self.table = data.sheets()[sheet]

    def readexcel(self,nrows=0,ncols=0,colnameindex=0):
        if (nrows == 0) and (ncols == 0):
            # 没有定义要读取的行数和列数就取excel中的行数和列数
             nrows = self.table.nrows
             ncols = self.table.ncols
             # print self.table.nrows
        colnames =  self.table.row_values(colnameindex)
        for row in range(1,nrows):
            rowdata = self.table.row_values(row)
            if rowdata:
                tmp = {}
                for i in range(0,len(colnames)):
                    tmp[colnames[i]] = rowdata[i]
                self.tabledata.append(tmp)
        return self.tabledata
    def readexcel2(self,nrows=0,ncols=0):
        if (nrows == 0) and (ncols == 0):
            # 没有定义要读取的行数和列数就取excel中的行数和列数
             nrows = self.table.nrows
             ncols = self.table.ncols
        for row in range(1,nrows):
                tmp = []
                for col in range(0,ncols):
                    tmp.append(self.table.cell(row,col).value)
                self.tabledata.append(tmp)
        return self.tabledata
    # def writeexcel(self,nrow,ncol,data):
    #     self.table.cell(nrow,ncol).value = data


if __name__ == "__main__":
    path = r'E:\woody\lijiale-zuoye1\web service\data\workbench.xlsx'
    e = OpExcel(path,0)
    data = e.readexcel()
    data1 = e.readexcel2()
    print data1