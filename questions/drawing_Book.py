#!/bin/python
#https://www.hackerrank.com/contests/w27/challenges/drawing-book/submissions/code/8228219
import sys


n = int(raw_input().strip())
p = int(raw_input().strip())
front = p/2
reverse = (n-p)/2
print(min(front,reverse))
