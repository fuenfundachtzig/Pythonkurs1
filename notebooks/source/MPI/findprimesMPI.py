# finde Primzahlen von pmin bis pmax
# MPI version
# Aufruf 
# findprimesMPI.py
#
import sys

def findprimes( pmin, pmax):

    primemax = 100000

    if primemax*primemax < pmax:
        print "Max prime :", primemax*primemax
        pmax = primemax*primemax

    # pmin odd
    if pmin%2 == 0:
        pmin +=1

    print "Finding primes from ", pmin, " to ", pmax

    # get ref list
    primeliste = [2, 3, 5, 7 ]
    p = 11
    while p < primemax:
        for t in primeliste:
            if p % t == 0 :
                break
            if t*t > p : # reached limit, must be prime
                primeliste.append(p)
                break
            #
        #
        p += 2

    # primes in specified range
    primeres = []
    p = pmin
    while p < pmax:
        for t in primeliste:
            if p % t == 0 :
                break
            if t*t > p : # reached limit, must be prime
                primeres.append(p)
                break
            #
        p += 2

#    print len(primeres)
#    print primeres[-10:]

    return primeres
# end function

# start main
from mpi4py import MPI
comm = MPI.COMM_WORLD

pmin = 3
nrange =  20000000
size = comm.size
index = comm.rank # start num according MPI rank
irange = nrange / size # split accdg # MPI nodes
pmin += index * irange
pmax = pmin + irange

result = findprimes( pmin, pmax)  # all nodes calculate their prime range

if comm.rank == 0 : # MPI master

    print 'MPI Master ', comm.size

    primall = []
    primall.append( result )

    for i in range(1,comm.size): # get data from nodes
        data = comm.recv( source=i )
        print 'Receiving from %d , N-primes = %d ' % ( i, len(data))
        primall.append(data)


    for r in primall:
        print len(r), r[:3], '...', r[-4:]

else: # MPI slaves
    comm.send( result, dest=0 ) # slaves just send




