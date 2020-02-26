#!/usr/bin/env python3
#
# A simple calculator server, accessible through XML-RPC
#

from xmlrpc.server import SimpleXMLRPCServer


class Calculator(object):
  def add(self, x, y):
    return x + y

  def sub(self, x, y):
    return x - y

  def mul(self, x, y):
    return x * y

  def div(self, x, y):
    return x / y

  def idiv(self, x, y):
    return x // y


def NoneFunc():
  return None


def HelloWorldFunc():
  return ["Hello", "World"]


def AddListFunc(lst):
  return sum(lst)


# create a new server instance
srv = SimpleXMLRPCServer(("", 7070), allow_none=True)

# register the XML-RPC introspection functions system.listMethods, system.methodHelp and system.methodSignature
srv.register_introspection_functions()

# register a function that can respond to XML-RPC requests
srv.register_function(NoneFunc, "none")
srv.register_function(HelloWorldFunc, "hw")
srv.register_function(AddListFunc, "addlist")
srv.register_function(lambda s: s, "echo")
srv.register_function(pow)

# register an object which is used to expose method names
srv.register_instance(Calculator())

# run the server's main loop
srv.serve_forever()
