#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import time

import gpxutil

tplist=[]

class TrackPoint(object):
    def __init__(self, lat, lon, elev, dtime, hrate):
        self.lat = float(lat)
        self.lon = float(lon)
        self.elev = float(elev)
        self.dtime = gpxutil.parsedate( dtime )
        self.hrate = int(hrate)
        self.dist = 0
        self.tdist = 0
        self.speed = 0
        self.x = 0
        self.y = 0

    def calcdist( self, pp ): 
        "calculate distance to previous point"
        (d,x,y) = gpxutil.distance( self.lat, self.lon, pp.lat, pp.lon )
        self.dist = d
        self.tdist = pp.tdist + self.dist 
        self.x = pp.x + x
        self.y = pp.y + y
        
    def calcspeed( self, tp ):
        "calculate speed, loop over list until time-diff >=5 s"
        pp = tp[0]
        if pp.dtime == None:
            return
        for tp in tp[1:]:
            dt = gpxutil.timediff( tp.dtime, pp.dtime)
            if ( dt != None and dt >= 5 ):
                self.speed = (tp.tdist - pp.tdist) / dt
                break

from xml.sax.handler import ContentHandler
class GPXHandler(ContentHandler):
    "A handler to deal with GPX data format"

    name = ""
    inTrkPt = 0
    tpinfo = {}

    def startElement(self, name, attrs):

        if name == "trkpt":
            lat = attrs.get("lat","")
            lon = attrs.get("lon","")
            self.tpinfo["lat"] = lat
            self.tpinfo["lon"] = lon
            self.inTrkPt = 1
        elif self.inTrkPt:
            self.name = name

    def characters(self, characters):

        if self.inTrkPt and self.name != None and len(self.name)>0 :
            self.tpinfo[self.name] = characters
            


    def endElement(self, name):
        namlist=[ "lat", "lon", "ele", "time", "gpxtpx:hr" ]


        self.name = None
        if name == "trkpt":
            self.inTrkPt = 0

            tpi = self.tpinfo
            # creat TrackPoint object and append to list
            a = TrackPoint( tpi["lat"], tpi["lon"], tpi["ele"], tpi["time"], tpi["gpxtpx:hr"] )
            tplist.append(a)

#            print
            self.tpinfo = {}
            
# 


import sys
from xml.sax import make_parser
# from simplehandler import ArticleHandler



ch = GPXHandler()
saxparser = make_parser()
saxparser.setContentHandler(ch)
saxparser.parse("GPS_example.gpx")
#saxparser.parse(sys.stdin)

ntp = len(tplist)

print (ntp, " Trackpunkte gefunden")

for i in range(1,ntp):
    tplist[i].calcdist( tplist[i-1] )

for i in range(1,ntp):
    tplist[i].calcspeed( tplist[i-1:] )
    
for tp in tplist:
    print ("%10.3f %10.3f %10.5f %10.1f %s" % (tp.dist, tp.tdist, tp.speed*3.6, tp.elev, tp.dtime))


# store info in straight arrays
tda = [ tp.tdist for tp in tplist ]
sa  = [ tp.speed*3.6 for tp in tplist ]
ea  = [ tp.elev for tp in tplist ]
hra = [ tp.hrate for tp in tplist ]
xa  = [ tp.x for tp in tplist ]
ya  = [ tp.y for tp in tplist ]



import pylab as pl

fig0 = pl.figure()
pl.subplot(3,1,1)
pl.title('Hoehenprofil')
pl.plot(tda, ea)

pl.subplot(3,1,2)
pl.title('Geschwindigkeit')
pl.plot(tda, sa)

pl.subplot(3,1,3)
pl.title('Herzfrequenz')
pl.plot(tda, hra)

fig3 = pl.figure()
pl.title('Herzfrequenz vs Geschwindigkeit')
pl.plot(sa, hra, '.')

fig4 = pl.figure()
pl.plot(xa, ya)

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

