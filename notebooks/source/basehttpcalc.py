#!/usr/bin/env python
# basehttpcalc.py -- a basic HTTP server / calculator

import http.server

class CalcHandler(http.server.BaseHTTPRequestHandler):

  def do_GET(self):
    path = self.path

    lst = path.split("/")
    if len(lst) != 4:
      self.send_response(403)
      self.end_headers()
      self.wfile.write(b"Illegal syntax. Use /{add,sub,mul,div}/num1/num2\r\n")
      return

    dummy, op, arg1, arg2 = lst

    if op not in ("add", "sub", "mul", "div"):
      self.send_response(403)
      self.end_headers()
      self.wfile.write(b"Illegal operation: %s\r\n" % op)
      return

    try:
      numarg1 = float(arg1)
      numarg2 = float(arg2)
    except ValueError:
      self.send_response(403)
      self.end_headers()
      self.wfile.write(b"Numerical arguments expected\r\n")
      return

    if op == "add":
      result = numarg1 + numarg2
    elif op == "sub":
      result = numarg1 - numarg2
    elif op == "mul":
      result = numarg1 * numarg2
    elif op == "div":
      if numarg2 == 0:
        result = "NaN"
      else:
        result = numarg1 / numarg2

    self.send_response(200)
    self.end_headers()
    self.wfile.write(str(result).encode())


def run_server(port=9092):
  server_class = http.server.HTTPServer
  server_address = ("", port)
  handler_class = CalcHandler

  server = server_class(server_address, handler_class)
  server.serve_forever()


if __name__ == "__main__":
  run_server()

