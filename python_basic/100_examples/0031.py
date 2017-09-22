#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 设该数为x：x + 100 = n^2, n^2 + 168 = m^2。
# 设m=n+k（不妨设m,n,k均为自然数）：带入m^2-n^2-168，得k^2+2nk=168。
# 解得n=84/k - k/2；由于n,k均为自然数，则nk>=1，故1< =k^2<168，故1<=k<=12。

for k in range(1, 13):
    n = 84/k -k/2
    if int(n) == n:
        #print n
        x = n ** 2 - 100
        print(x)