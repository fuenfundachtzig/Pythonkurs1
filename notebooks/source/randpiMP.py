# calcuate Pi counting random hits in circle of radius 1
# converted from threading to multiprocessing
# doesn't give correct results
# 
import multiprocessing
import random
import sys

class RandPi( multiprocessing.Process ) :
    """
    A sample Process class
    """
    def __init__(self, nit):
        """
        Constructor, setting initial variables
        """
        self.nit = nit
        self.count = 0
        multiprocessing.Process.__init__(self, name="RandPi")
        
    def run(self):
        """
        overload of multiprocessing.Process.run()
        main control loop
        """
        #print("%s starts" % (self.getName(),)) <- does not exist for Process

        for i in range(self.nit):
            if ( random.random()**2 + random.random()**2 < 1. ):
                self.count += 1
        print("Process result in run:", self.count)


def main():
    nit = 1000000
    nth = 2
    if len(sys.argv)>1:
        nit = int(sys.argv[1])
    if len(sys.argv)>2:
        nth = int(sys.argv[2])

    # create & start threads
    tha = []
    for i in range(nth):
        pth = RandPi(nit)
        pth.start()
        tha.append(pth)

    # wait threads to finish and sum up counts
    psum = 0
    for pth in tha:
        pth.join()
        print("Got result from process:", pth.count)
        psum += pth.count

    piest = 4.*float(psum) / ( nit * nth )
    print('Pi = ', piest)



if __name__ == "__main__" :
    main()
