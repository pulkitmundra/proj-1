#!/usr/bin/python

import os
import cgi,cgitb

print("Content-type: text/html\r\n\r\n")


form = cgi.FieldStorage() 
if form.getvalue('opt'):
   opt = form.getvalue('opt')
if form.getvalue('nodn'):
   nodn = form.getvalue('nodn')

f=open('sess.txt','r')
udata=f.read()
f.close()	
unamedata=udata.split(':')[0]


if opt=="ndata":
	os.system('sudo cat clusters.txt | grep "'+unamedata+':" | wc -l > output.txt')
	f=open('output.txt','r')
	check=f.read()
	f.close()
	for i in range(int(check)):
		os.system('sudo docker kill '+unamedata+'_'+str(i)+' > output1.txt')
		os.system('sudo docker rm '+unamedata+'_'+str(i)+' > output2.txt')
	os.system('sudo cat clusters.txt | grep -v "'+unamedata+':" > output.txt')
	os.system('sudo cat output.txt > clusters.txt')

	print int(nodn)

    	for i in range(int(nodn)):
		
		name=unamedata+"_"+str(i)
		os.system('sudo docker run -id --name '+name+' newcento > output3.txt')

		f = open('clusters.txt','a')
		f.write(unamedata+':'+name+'\n')
		f.close()


	print "NEW CLUSTER IS NOW AVAILABLE!!"
	print "<marquee> New Cluster are available from now on.</marquee>"
	print "<pre>"
	print "<h2><a href='/hvsv2.html'>BACK</a></h2><h2><a href='/loggedin.html'>HOME</a></h2>"
	print "</pre>"

if opt=="adata":
	os.system('cat clusters.txt | grep "'+unamedata+':" | wc -l > output.txt')
	f=open('output.txt','r')
	check=f.read()
	f.close()
		
	for i in range(int(nodn)):
		name=unamedata+"_"+str(i+int(check))
		qry = 'sudo docker run -itd --name '+name+' newcento > output3.txt'
		os.system(qry)
		f = open('clusters.txt','a')
		f.write(unamedata+':'+name+'\n')
		f.close()
		
	print "DATANODES ADDED TO THE CLUSTER !!"
	print "<marquee> New datanodes are available from now on.</marquee>"
	print "<pre>"
	print "<h2><a href='/hvsv2.html'>BACK</a></h2><h2><a href='/loggedin.html'>HOME</a></h2>"
	print "</pre>"


if opt=="rdata":
	os.system('sudo cat clusters.txt | grep "'+unamedata+':" | wc -l > output.txt')
	f=open('output.txt','r')
	check=f.read()
	f.close()
	for i in range(int(check)):
		os.system('sudo docker kill '+unamedata+'_'+str(i)+' > output1.txt')
		os.system('sudo docker rm '+unamedata+'_'+str(i)+' > output2.txt')
	os.system('sudo cat clusters.txt | grep -v "'+unamedata+':" > output.txt')
	os.system('sudo cat output.txt > clusters.txt')
	#os.system('sudo hdfs dfs -rm -Rf /'+unamedata+'/*')
	print "CLUSTER DELETED !!"
	print "<marquee> Deleting Cluster Also deletes your existing files in the cluster.</marquee>"
	print "<pre>"
	print "<h2><a href='/hvsv2.html'>BACK</a></h2><h2><a href='/loggedin.html'>HOME</a></h2>"
	print "</pre>"

