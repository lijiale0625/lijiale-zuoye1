#coding:utf-8
#import numpy as np
import pylab as pl
x = [1, 2, 3, 4, 5]# Make an array of x values
y = [1, 4, 1, 16, 2]# 2 an array of y values for each x value
pl.plot(x, y)# use pylab to plot x and y
pl.show()# show the plot on the screen
# 2.1.2 ɢ��ͼ Scatter plots
# ��pl.plot(x, y)�ĳ�pl.plot(x, y, 'o')���ɣ���ͼ����ɫ�汾
# ��ɫ����pl.plot(x, y, 'o')�ĳ�pl.plot(x, y, ��or��)