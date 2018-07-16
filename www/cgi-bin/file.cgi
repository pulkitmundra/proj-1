#!/usr/bin/python2

import cgi
import cgitb
import commands
cgitb.enable()

print "context-type:text/html"
print ""

html_data=cgi.FieldStorage()

nn=html_data.getvalue('nn')
dn1=html_data.getvalue('dn1')
dn2=html_data.getvalue('dn2')
dn3=html_data.getvalue('dn3')

#print "helloworld"
print nn
print dn1
print dn2
print dn3

if nn == "nn" :
	commands.getoutput("sudo virsh start nn")

if dn1 == "dn1" :
        commands.getoutput("sudo virsh start dn1")

if dn2 == "dn2" :
        commands.getoutput("sudo virsh start dn2")

if dn3 == "dn3" :
        commands.getoutput("sudo virsh start dn3")


