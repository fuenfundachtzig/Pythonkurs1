# calcuate Pi counting random hits in circle of radius 1
# using multiprocessing and communication
# 
import multiprocessing
import random
import sys

class RandPi( multiprocessing.Process ) :
    """
    A sample Process class
    """
    def __init__(self, nit, res_queue):
        """
        Constructor, setting initial variables
        """
        self.nit = nit
        self.count = 0
        self.res_queue = res_queue
        multiprocessing.Process.__init__(self)
        
    def run(self):
        """
        overload of multiprocessing.Process.run()
        main control loop
        """
        for i in range(self.nit):
            if ( random.random()**2 + random.random()**2 < 1. ):
                self.count += 1

        self.res_queue.put( self.count ) # put result in queue
        

def main():
    nit = 1000000
    nth = 2
    if len(sys.argv)>1:
        nit = int(sys.argv[1])
    if len(sys.argv)>2:
        nth = int(sys.argv[2])

    # create & start processes
    results = multiprocessing.Queue() # needed for communication of results
    tha = []
    for i in range(nth):
        pth = RandPi(nit, results)
        pth.start()
        tha.append(pth)

    # wait for processes to finish and sum up counts
    psum = 0
    for pth in tha:
        pth.join()
        result = results.get()
        print("Got result from process:", result)
        psum += result

    piest = 4.*float(psum) / ( nit * nth )
    print('Pi = ', piest)


if __name__ == "__main__" :
    main()
