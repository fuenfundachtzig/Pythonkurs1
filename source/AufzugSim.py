import threading
import time
import random

class AufzugSim( threading.Thread ) :
    """
    A sample thread class
    """
    NSTOCK = 4
    NPERSON = 5
    TSLEEP = 20 
    global stop
    stop = False  # global flag 
    
    def __init__(self, num, aufz, lck, name="TestThread"):
        """
        Constructor, setting initial variables
        """
        threading.Thread.__init__(self, name=name)
        self.aufz = aufz
        self.id   = num
        self.lck = lck

        self.stock = 0
        
    def run(self):
        """
        overload of threading.thread.run()
        main control loop
        """

        while ( not stop ) :
            newstock = random.randint(0, self.NSTOCK) # create random int between 0 and NSTOCK

            if newstock != self.stock:
                s1 = time.time() # get start-time
                self.lck.acquire() # get lock, waits until it's free
                self.aufz.travel( self.stock, newstock ) # hol und fahr Aufzug
                self.lck.release() # release lock
                print("Person  %d travelled from %d  to %d  in %6.0f" % ( self.id,  self.stock, newstock, 1000*(time.time() - s1) ))
                self.stock = newstock
            #
            sleeptime = random.randint(0, self.TSLEEP)
            time.sleep(sleeptime/1000.) # simuliere Arbeitszeit
        #
    pass


class Aufzug :
    def __init__(self):
        self.floor = 0
        self.TIMESCALE = 0.5 # 0.5 sec
   
    def travel( self, stock, newfloor ) :
        traveltime = abs( stock - self.floor ) # Zur Person fahren
        time.sleep( traveltime * self.TIMESCALE )
        self.floor = stock;
        traveltime = abs( newfloor - stock )# Zum neuen Stock fahren
        time.sleep( traveltime * self.TIMESCALE )
        self.floor = newfloor



meinAufzug = Aufzug() 
lck = threading.Lock()
al = []

for i in range(AufzugSim.NPERSON) :
    az = AufzugSim( i, meinAufzug, lck)
    al.append( az )
    az.start() # start Person Threads

time.sleep(120.) # main thread sleep for 2 mins
stop = True # set stop flag
