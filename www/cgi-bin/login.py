#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb 
import os

def inpu(x):
   fo=open('nap.txt','a')
   fo.write(x)
   fo.close()
   return

# Create instance of FieldStorage 
form = cgi.FieldStorage() 
print("Content-type: text/html\r\n\r\n")

uname=''
upass=''
##Get data from fields
if form.getvalue('upass'):
   upass = form.getvalue('upass')
if form.getvalue('uname'):
   uname = form.getvalue('uname')
if form.getvalue('login'):
   flag=0
   f=open('nap.txt','r')
   x=f.read()
   f.close()
   for i in x.split():
      if i==(uname+":"+upass):
         x=uname+":"+upass
         x=str(x)
         os.system('./sess.py '+x)
	 print "Your Account has been verified."
	 print "<marquee>Select Next to Proceed.</marquee>"
         print "<a href='/loggedin.html'<a>NEXT</a>"
	 flag=1
   if flag==0:
	 print "WRONG CREDENTIALS!!\n"
	 print "<marquee>Please try with your correct account details!!</marquee>"
       	 print "<a href='/login-reg.html'> BACK </a>"
if form.getvalue('signup'):

   f=open('nap.txt','r')
   data=f.read()
   f.close()
   flag=0

   udata=data.split('\n')

   for s in udata:
   	unamedata=s.split(':')[0]
	if unamedata==uname:
		flag=1
		break
   if flag==1:
	print "Username Already Exists !!\n"
	print "<marquee>Please try some other UserName !!</marquee>"
	print "<a href='/login-reg.html'> BACK </a>"
   else:
	   f=open('nap.txt','a')
	   f.write(uname+":"+upass+"\n")
	   f.close()
	   f=open('sess.txt','w')
	   f.write(uname+":"+upass+"\n")
	   f.close()
	   print "Your Account has been initiated."
	   print "<marquee>Select Next to Proceed.</marquee>"
	   print "<a href='/loggedin.html'<a>NEXT</a>"
