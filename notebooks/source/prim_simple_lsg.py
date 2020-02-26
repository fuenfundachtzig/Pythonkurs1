#!/usr/bin/env python

num = int(raw_input("Enter a number: "))
i = 2
while (i < num):
    if (num%i)==0:
        print '%s is not a prim' %num
        break
    i+=1
else:
    print '%s is a prim' %num
