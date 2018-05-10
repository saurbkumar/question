#time - 20 min
#https://www.hackerrank.com/challenges/sherlock-and-squares

# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import ceil,floor
n = int(raw_input())
for _ in range(n):
    a = map(int,raw_input().split())
    lower_num = ceil(float(a[0])**.5)
    upper_num = floor(float(a[1])**.5);
    if upper_num - lower_num <0:
        print 0
    else:
        print int(upper_num - lower_num) + 1
