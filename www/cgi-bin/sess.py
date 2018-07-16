#!/usr/bin/python
import sys
f=open('sess.txt','w')
f.write(sys.argv[1:][0]+"\n")
f.close()
