#!/usr/bin/env python3
#
# A threaded XML-RPC server.
#

from xmlrpc.server import SimpleXMLRPCServer
from socketserver import ThreadingMixIn
from time import sleep


def SlowFunc():
  sleep(5)
  return 42


count = 0


def FastFunc():
  "ignoring potential race conditions here"
  global count
  count = count + 1
  return count


# define our server using the threading "mix-in"
class ThreadedSimpleXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):
  pass


# set up multi-threaded server
srv = ThreadedSimpleXMLRPCServer(("", 7070), allow_none=True)

# register functions
srv.register_introspection_functions()
srv.register_function(SlowFunc)
srv.register_function(FastFunc)

# start server
srv.serve_forever()
