#coding:utf-8
#import numpy as np
import pylab as pl
x = [1, 2, 3, 4, 5]# Make an array of x values
y = [1, 4, 1, 16, 2]# 2 an array of y values for each x value
pl.plot(x, y)# use pylab to plot x and y
pl.show()# show the plot on the screen
# 2.1.2 散点图 Scatter plots
# 把pl.plot(x, y)改成pl.plot(x, y, 'o')即可，下图的蓝色版本
# 红色：把pl.plot(x, y, 'o')改成pl.plot(x, y, ’or’)