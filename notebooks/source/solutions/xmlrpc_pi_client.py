#!/usr/bin/env python
import xmlrpclib
import socket

if __name__ == "__main__" :
    prx1 = xmlrpclib.ServerProxy('http://localhost:7070', allow_none=True, verbose=False)

    prx2 = xmlrpclib.ServerProxy('http://staufen:7070', allow_none=True, verbose=True)

    try:
        print prx1.calcpi()
    except socket.error:
        print 'One host is down !'

    try:
        print prx2.calcpi()
    except:
        print 'One host is down !'

    print "That's all, folks!"
