#!/usr/bin/python
import os
import cgi,cgitb

print("Content-type: text/html\r\n\r\n")

f=open('sess.txt','r')
udata=f.read()
f.close()	
unamedata=udata.split(':')[0]

os.system('cat clusters.txt | grep "'+unamedata+':" | wc -l > output.txt')
f=open('output.txt','r')
check=f.read()
f.close()

for i in range(int(check)):
	os.system('sudo docker exec '+unamedata+'_'+str(i)+' hadoop-daemon.sh start datanode > output1.txt')
