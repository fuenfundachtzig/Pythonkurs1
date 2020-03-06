from SocketServer import TCPServer, StreamRequestHandler


class EchoHandler(StreamRequestHandler):
  def handle(self):
    print "Serving client:", self.client_address
    for line in self.rfile:
      self.wfile.write("S:" + str(eval(line))) 
      # Running arbitrary user input through eval poses an obvious security problem.
      # While eval() (in contrast to exec()) only accepts and evaluates expressions (and not statements) 
      # so that a naive "import os" fails with a syntax error, you may be surprised to learn that 
      # there is a function "__import__" that does the same, i.e. 
      #   'eval('__import__("subprocess").getoutput("ls")')
      # will show the content of the current directory. 
      # And allow malicious users to do anything they want remotely on your computer.

TCPServer.allow_reuse_address = True
srv = TCPServer(("", 7070), EchoHandler)
srv.serve_forever()
