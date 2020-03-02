import sys


import urllib.request
# open Kant's Text
# f=urllib2.urlopen("http://www-static.etp.physik.uni-muenchen.de/kurs/Computing/python/source/kant.txt")
f=urllib.request.urlopen("https://goo.gl/rGqW4k")


# urlopen gives byte-stream, must convert into unicode
lines = [ z.decode('utf-8') for z in f.readlines() ]


# split into words
words=[]

#for line in f: # iteriere ueber alle Zeilen
#    words += line.split() # packe Words in list

# Plain reading
#words=[ word for line in lines for word in line.split() ]



import string
# use strip method with punctuation to get rid of comma, etc
#words=[ word.strip(string.punctuation) for line in lines for word in line.split() ]


import re
# use re.findall to get bare words 
words=[ word for line in lines for word in re.findall(r'(\b\w+\b)',line) ]


from collections import Counter
word_counts=Counter(words)

print (word_counts["Vernunft"])

