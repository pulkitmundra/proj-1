#!/usr/bin/python
import os
import cgi,cgitb

print("Content-type: text/html\r\n\r\n")

unamedata="messi"
name=unamedata+"_"+str(0)
qry = 'sudo docker run -itd --name '+name+' newcento > output.txt'
os.system(qry)
f = open('clusters.txt','a')
f.write(unamedata+':'+name+'\n')
f.close()

print "YO"
