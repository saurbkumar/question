#time 1 hr

https://www.hackerrank.com/challenges/taum-and-bday


import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    b,w = raw_input().strip().split(' ')
    b,w = [long(b),long(w)]
    x,y,z = raw_input().strip().split(' ')
    x,y,z = [long(x),long(y),long(z)]
    print min(b*x+w*y,(b*(y+z))+w*y,b*x+(w*(x+z)))
