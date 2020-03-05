#!/usr/bin/env python3

from pickle import load, dump

if __name__ == "__main__" :

    data = {}

    # Read in data.txt
    f = open('data.txt')
    lines = f.readlines()
    f.close()
    for line in lines:
        temp = line.split(' ')
        data[temp[1].strip()] = [temp[0].strip(), temp[2].strip(), temp[3].strip()]

    # Save data to data.pickle
    out = open('data.pickle','wb')
    dump(data,out)
    out.close()

    # Read back data
    inp = open('data.pickle','rb')
    newdata = load(inp)
    inp.close()

    # Sort last names
    names = list(newdata.keys())
    names.sort()

    # Print to screen
    for i in names:
        print(i, newdata[i])
