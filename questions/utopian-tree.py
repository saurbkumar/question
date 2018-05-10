#https://www.hackerrank.com/challenges/utopian-tree

#time - 1 hour

#!/bin/python

import sys

hght_tree= 1
t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    curr_len = hght_tree
    if n==0:
        curr_len = curr_len
    else:
        if n%2==0:
            for _ in range(n/2):
                a = curr_len*2
                curr_len = a+1
        else:
            for _ in range(n/2):
                a = curr_len*2
                curr_len = a+1
            curr_len = curr_len * 2
    print curr_len
