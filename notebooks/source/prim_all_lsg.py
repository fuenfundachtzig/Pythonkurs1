#!/usr/bin/env python

import math

num = int(raw_input("Enter a number: "))
i = 2
loops = 0;

primes=[]

for testnum in xrange(2,num):
    i = 2
    prim = True
    #while (i < math.floor(math.sqrt(testnum)+1)):
    while (i < testnum):
        loops += 1
        if (testnum%i)==0:
            prim = False
            break
        i+=1
    if prim:
        primes.append(testnum)


print primes
print "Anzahl = ", len(primes)
print "Schleifen = ", loops
