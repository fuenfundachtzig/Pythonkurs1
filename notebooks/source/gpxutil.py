
import math
import datetime

ERD_RADIUS = 6378 * 1000


def distance( lat_1, long_1 , lat_2, long_2 ):
    coef = math.cos(lat_1 / 180. * math.pi)
    x = lat_1 - lat_2
    y = (long_1 - long_2) * coef

    fact = math.pi/180. * ERD_RADIUS

    dist = math.sqrt(x * x + y * y) * fact
    return dist, x*fact, y*fact

def parsedate( dstring ):
    try:
        d=datetime.datetime.strptime( dstring,'%Y-%m-%dT%H:%M:%SZ')
    except:
        print("Trouble converting date ", dstring)
        d = None

    return d


def timediff( date_1, date_2 ):
    try:
        diff=(date_1-date_2).total_seconds()
    except:
        print("can't get date difference for", date_1, date_2)
        diff=None

    return diff

