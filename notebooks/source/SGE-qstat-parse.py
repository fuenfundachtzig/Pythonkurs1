#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import time

from xml.sax.handler import ContentHandler
class SGEQueueHandler(ContentHandler):
    #A handler to deal with articles in XML
    #    def startElement(self, name, attrs):
    #    print Start element:, name
    name = ""
    inBody = 0
    inRunJob = 0
    jobinfo = {}

    def startElement(self, name, attrs):
        # print "startElement", name
        if name == "job_list":
            state = attrs.get("state","")
            if state == "running" :
                self.inRunJob = 1
        elif self.inRunJob:
            self.name = name

    def characters(self, characters):
        # print "characters", characters

        if self.inRunJob and self.name != None and len(self.name)>0 :
            self.jobinfo[self.name] = characters
            
            # print self.name, characters

    def endElement(self, name):
        namlist=[ "cpu_usage", "WallT", "JAT_start_time", "queue_name",
                  "JB_owner" , "JB_job_number"]

        # print "endElement", name
        self.name = None
        if name == "job_list":
            self.inRunJob = 0
            # print self.jobinfo

            for nam in namlist:
                
                try:
                    print(nam, ' = ',  self.jobinfo[nam], " , ", end=' ')
                except:
                    print("None", " , ", end=' ')
            
            print()
            self.jobinfo = {}
            
# 


import sys
from xml.sax import make_parser
# from simplehandler import ArticleHandler


global tnow
tnow = time.localtime()

ch = SGEQueueHandler()
saxparser = make_parser()
saxparser.setContentHandler(ch)
#saxparser.parse("qstat-example.xml")
saxparser.parse(sys.stdin)


# sexam = """<?xml version='1.0'?>
# <job_info  xmlns:xsd="http://www.w3.org/2001/XMLSchema">
#   <queue_info>
#     <job_list state="running">
#       <JB_job_number>4187521</JB_job_number>
#       <JAT_prio>0.50000</JAT_prio>
#       <JAT_ntix>0.00000</JAT_ntix>
#       <JB_name>STDIN</JB_name>
#       <JB_owner>atlasprd</JB_owner>
#       <JB_project>lcg</JB_project>
#       <JB_department>lcg</JB_department>
#       <state>r</state>
#       <JAT_start_time>2009-07-21T18:52:26</JAT_start_time>
#       <cpu_usage>40.00000</cpu_usage>
#       <mem_usage>2.11964</mem_usage>
#       <io_usage>0.00000</io_usage>
#       <tickets>0</tickets>
#       <JB_override_tickets>0</JB_override_tickets>
#       <JB_jobshare>0</JB_jobshare>
#       <otickets>0</otickets>
#       <ftickets>0</ftickets>
#       <stickets>0</stickets>
#       <JAT_share>0.00000</JAT_share>
#       <queue_name>lcg-long@lx64e173.cos.lrz-muenchen.de</queue_name>
#       <master>MASTER</master>
#       <slots>1</slots>
#     </job_list>
#   </queue_info>
#   <job_info>
#   </job_info>
# </job_info>"""

# p.Parse(sexam,1)

