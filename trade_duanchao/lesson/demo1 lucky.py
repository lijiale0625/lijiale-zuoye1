#coding:gbk
import random
file=open("lucky.txt","a+")

x=int(raw_input("下几注："))
for i in range(x):
	red=random.sample(range(1,34,1),6)
	blue=random.sample(range(1,17,1),1)
	red.sort()
	print ('red: ',red,'blue:',blue)
	file.writelines(str(red))
	file.writelines(str(blue))
	file.writelines("\n")
file.close()	
