class MyType(object):
    message='Hallo'
    num = 123
    def hello(self):
        return self.message+' '+str(self.num)
