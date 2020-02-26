#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import time

tplist=[]

from xml.sax.handler import ContentHandler
class GPXHandler(ContentHandler):
    #A handler to deal with articles in XML
    #    def startElement(self, name, attrs):
    #    print Start element:, name
    name = ""
    inTrkPt = 0
    tpinfo = {}

    def startElement(self, name, attrs):
        # print "startElement", name
        if name == "trkpt":
            lat = attrs.get("lat","")
            lon = attrs.get("lon","")
            self.tpinfo["lat"] = lat
            self.tpinfo["lon"] = lon
            self.inTrkPt = 1
        elif self.inTrkPt:
            self.name = name

    def characters(self, characters):
        # print "characters", characters

        if self.inTrkPt and self.name != None and len(self.name)>0 :
            self.tpinfo[self.name] = characters
            
            # print self.name, characters

    def endElement(self, name):
        namlist=[ "lat", "lon", "ele", "time", "gpxtpx:hr" ]

        # print "endElement", name
        self.name = None
        if name == "trkpt":
            self.inTrkPt = 0
#            print self.tpinfo

            for nam in namlist:
                
                try:
                    print(nam, ' = ',  self.tpinfo[nam], " , ", end=' ')
                except:
                    print("None", " , ", end=' ')


            tplist.append( self.tpinfo )
            self.tpinfo = {}
#

import sys
from xml.sax import make_parser
# from simplehandler import ArticleHandler


global tnow
tnow = time.localtime()

ch = GPXHandler()
saxparser = make_parser()
saxparser.setContentHandler(ch)
saxparser.parse("GPS_example.gpx")
#saxparser.parse(sys.stdin)

ntp = len(tplist)

print(ntp, " Trackpunkte gefunden")

# store info in straight arrays: ele == Hoehe
ea  = [ float(tp["ele"]) for tp in tplist ]



import pylab as pl

pl.title('Hoehenprofil')
pl.plot(list(range(ntp)), ea)

pl.show()


# <gpx xmlns="http://www.topografix.com/GPX/1/1"
# ... 
# <trk><name>GPX-example</name>
# <extensions><gpxx:TrackExtension>
# <gpxx:DisplayColor>Blue</gpxx:DisplayColor>
# </gpxx:TrackExtension></extensions>
# <trkseg>
# <trkpt lat="47.5788825285" lon="10.5603028927">
# <ele>865.32</ele>
# <time>2014-06-15T08:02:21Z</time>
# <extensions><gpxtpx:TrackPointExtension>
# <gpxtpx:hr>68</gpxtpx:hr></gpxtpx:TrackPointExtension></extensions>
# </trkpt>
# ...


# p.Parse(sexam,1)

