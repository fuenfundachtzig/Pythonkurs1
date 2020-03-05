#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import time

from xml.sax.handler import ContentHandler
class SGEQueueHandler(ContentHandler):
    "A handler to deal with SGE quese statistics data in XML"

    name = ""
    inBody = 0
    inRunJob = 0
    jobinfo = {}
    jobinfo_list = []


    def startElement(self, name, attrs):
        if name == "job_list":
            state = attrs.get("state","")
            if state == "running" :
                self.inRunJob = 1
        elif self.inRunJob:
            self.name = name

    def characters(self, characters):

        if self.inRunJob and self.name != None and len(self.name)>0 :
            if self.name  == "queue_name": # extract host from lcg-long@lx64e197.cos.lrz-muenchen.de
                try:
                    n1 = characters.find('@') + 1
                    n2 = characters[n1:].find('.') + n1
                    self.jobinfo[self.name] = characters[n1:n2]
                except:
                    self.jobinfo[self.name] = "Failed conversion"
                    
            elif self.name  == "JAT_start_time" :
                self.jobinfo[self.name] = characters
                try:
                    t=time.strptime(characters,"%Y-%m-%dT%H:%M:%S")
                    deltat = time.mktime(tnow)-time.mktime(t)
                    self.jobinfo['WallT'] = deltat
                except:
                    self.jobinfo['WallT'] = "Failed conversion"
                    
            else:
                self.jobinfo[self.name] = characters
            

    def endElement(self, name):
        namlist=[ "cpu_usage", "WallT", "Eff", "JAT_start_time", "queue_name",
                  "JB_owner" , "JB_job_number"]

        self.name = None
        if name == "job_list":
            self.inRunJob = 0

            for nam in namlist:
                if nam == "Eff" :
                    try:
                        val = float(self.jobinfo["cpu_usage"]) / float(self.jobinfo["WallT"])
                    except:
                        val = None
                    self.jobinfo[nam] = val
                
                try:
                    print (nam, ' = ',  self.jobinfo[nam], " , " , end='')
                except:
                    print ("None", " , "  , end='')
            
            print (' ')
            self.jobinfo_list.append( self.jobinfo )
            self.jobinfo = {}
            
# 



def main():
    import sys
    from xml.sax import make_parser
    # from simplehandler import ArticleHandler


    global tnow
    # tnow = time.localtime()
    tnow = time.strptime('Tue Jul 28 15:10:34 2009')

    global ch
    ch = SGEQueueHandler()
    saxparser = make_parser()
    saxparser.setContentHandler(ch)
    saxparser.parse("SGE-qstat.xml")
    # saxparser.parse(sys.stdin)

    # extract efficiency
    ea = [ j['Eff'] for j in ch.jobinfo_list if j['Eff'] != None ]
    print (ea)

    import pylab as pl
    pl.hist( ea, bins=100 )
    #pl.yscale('log')
    pl.show()

if __name__ == '__main__':
    main()

