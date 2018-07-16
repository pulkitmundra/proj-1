#!/usr/bin/python
import os
import cgi,cgitb

print("Content-type: text/html\r\n\r\n")

f=open('sess.txt','r')
a=f.read()
f.close()

a=a.split(':')
a=a[0]+'_dn_'
print a

os.system('sudo docker ps | grep '+a+' > docktemp.txt')


os.system('sudo cat docktemp.txt | wc -l > docktempp.txt')

f=open('docktempp.txt','r')
n=f.read()
print n
f.close()
n=int(n)

os.system('sudo docker ps > docktemp.txt')

f=open('docktemp.txt','r')
b=f.read()
f.close()
z=b.split('\n')

#print z[1:]

for i in range(1,n+1):
	y=z[i].split('        ')
	idd=y[0]
	l=y[4]
	print l+"<br>"
	print idd+"<br>"
	os.system('sudo docker exec '+idd +' hostname -i > docktemp.txt')
	f=open('docktemp.txt','r')
	c=f.read()
	f.close()
	print c+"<br><br>"
