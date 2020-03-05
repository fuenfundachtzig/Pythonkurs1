from SocketServer import TCPServer, StreamRequestHandler


class EchoHandler(StreamRequestHandler):
  def handle(self):
    print "Serving client:", self.client_address
    for line in self.rfile:
      self.wfile.write("S:" + str(eval(line)))


TCPServer.allow_reuse_address = True
srv = TCPServer(("", 7070), EchoHandler)
srv.serve_forever()
