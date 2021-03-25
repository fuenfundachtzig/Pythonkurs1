#!/usr/bin/env python
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SocketServer import ThreadingMixIn
import numpy
import numpy.random
from numpy.core import *

def calcpi():
    num = 1000000
    rx = numpy.random.random(num)
    ry = numpy.random.random(num)
    r = numpy.sqrt(rx**2 + ry**2)
    return float(len(where(r<1)[0]))/len(r)

class ThreadedSimpleXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer): pass

if __name__ == "__main__" :
    srv = ThreadedSimpleXMLRPCServer(('', 7070), allow_none=True)
    srv.register_introspection_functions()
    srv.register_function(calcpi)

    srv.serve_forever()
