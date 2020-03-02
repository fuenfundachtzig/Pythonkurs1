#!/usr/bin/env python

s   = input('Source string: ')
sub = input('substring: ')

if sub in s:
    print ("'%s' is a substring of '%s'" % (sub, s))
else:
    print ("'%s' is NOT a substring of '%s'" % (sub, s))

try:
    idx = s.index(sub)
    ridx = s.rindex(sub)
    print ("'%s'.index('%s') == %d" % (s, sub, idx))
    print ("'%s'.rindex('%s') == %d" % (s, sub, ridx))
except ValueError:
    print ("'%s' doesn't occur in '%s'" % (sub, s))

pos = s.find(sub)
rpos = s.rfind(sub)
print ("'%s'.find('%s') == %d" % (s, sub, pos))
print ("'%s'.rfind('%s') == %d" % (s, sub, rpos))

print ("'%s'.startswith('%s') == " % (s, sub), s.startswith(sub))
print ("'%s'.endswith('%s') == " % (s, sub), s.endswith(sub))

print ("'%s' occurs %d times in '%s'" % (sub, s.count(sub), s))
