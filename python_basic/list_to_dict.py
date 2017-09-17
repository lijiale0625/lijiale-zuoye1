
a=[('1', '1'), ('2', '1'), ('3', '1')]
b = [('1', '1'), ('2', '1'), ('3', '1')]
c=[('3', '21609'), ('1', '1'), ('2', '1')]
d = [a,b,c]

result=[]
for list in d:
    print dict(list)
    result.append(dict(list))
print result