#!/usr/bin/env python3
#
# A simple XML-RPC client of the calculator server.
#

import xmlrpc.client

# setup ServerProxy instance which manages communication with the remote XML-RPC server
prx = xmlrpc.client.ServerProxy("http://localhost:7070", allow_none=True, verbose=False)

# send requests to server
print(prx.none())
print(prx.hw())
print(prx.echo("Hello, XML-RPC World!"))

# send requests to server (computations)
print(prx.addlist([5, 6, 7, 8, 9, 10]))
print(prx.add(3, 2), prx.sub(3, 2), prx.mul(3, 2), prx.div(7, 2), prx.idiv(7, 2))
print(prx.pow(2, 3))

# call a non-existing function
try:
  print(prx.bug())
except xmlrpc.client.Fault as f:
  print(f)

# provoke another error
try:
  print(prx.idiv(3, 0))
except xmlrpc.client.Fault as f:
  print(f)

# list remote methods
print("List of remote methods:")
print("\n".join(["  " + meth for meth in prx.system.listMethods()]))
