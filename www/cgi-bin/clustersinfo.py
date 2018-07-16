#!/usr/bin/python
import os
import cgi,cgitb

print("Content-type: text/html\r\n\r\n")

f=open('sess.txt','r')
udata=f.read()
f.close()	
unamedata=udata.split(':')[0]

os.system('sudo cat clusters.txt | grep "'+unamedata+':" | wc -l > output.txt')
f=open('output.txt','r')
check=f.read()
f.close()

print "<pre>"
print "<h2>CLUSTER OWNER : </h2>"+unamedata
print "<h2>NUMBER OF DATANODES : </h2>"+check

for i in range(int(check)):
	print "<br><br><h3>MACHINE "+str(i)+"</h3>"
	os.system('sudo docker exec '+unamedata+'_'+str(i)+' hostname -i > output1.txt')
	f=open('output1.txt','r')
	c=f.read()
	f.close()
	print "<h4>IP ADDRESS : </h4>"+c

print "<h2><a href='/loggedin.html'>BACK</a></h2><h2><a href='/loggedin.html'>HOME</a></h2>"
