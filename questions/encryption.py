#time = 40min
#https://www.hackerrank.com/challenges/encryption
from math import ceil,floor
import sys
s = raw_input().strip()
cont = 0
s = s.replace(" ", "")
row = int(floor(len(s)**.5))
colm = int(ceil(len(s)**.5))
for x in range(colm):
    temp = s[x::colm]
    print temp, 
