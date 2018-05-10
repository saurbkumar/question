#time - 15 min
#https://www.hackerrank.com/contests/w28/challenges/boat-trip
#!/bin/python

import sys


n,c,m = raw_input().strip().split(' ')
n,c,m = [int(n),int(c),int(m)]
p = map(int, raw_input().strip().split(' '))
prnt = None
for i in p:
    if c*m < i:
        prnt = False
        break
if prnt==False:
    print "No"
else:
    print "Yes"
