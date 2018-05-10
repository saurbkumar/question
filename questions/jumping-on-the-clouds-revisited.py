#https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited
#time - 36 Min

#!/bin/python

import sys


n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
c = map(int,raw_input().strip().split(' '))
i = 0
e = 100#energy
while True:
    if(c[i]==1):# thunder cloud
        e = e-3
    else:
        e = e-1
    i = (i+k)%n
    if(i==0):
        break
print e
