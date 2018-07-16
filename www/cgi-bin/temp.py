#!/usr/bin/python
import os
f = open('/hadoop2/etc/hadoop/core-site.xml','rw')
x=f.read()
f.close()
y=x[817:820].split(':')
print y[0]
l="12:"+str(y[1])+str(x[820:])
l=str(x[:817])+l
f=open('xyz.txt','w')
f.write(l)
f.close()
