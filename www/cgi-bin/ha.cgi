#!/usr/bin/python

import  cgi,cgitb,os,time,commands,sys
cgitb.enable()
print  "content-type:text/html"
print  ""

html_data=cgi.FieldStorage()
k=html_data.getvalue("hd")

if k=='hv1':


	print "<meta  http-equiv='refresh' content='0;url=http://192.168.122.1/hadd.html'/>"
