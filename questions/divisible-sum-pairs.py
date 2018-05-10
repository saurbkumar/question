#https://www.hackerrank.com/challenges/linkedin-practice-divisible-sum-pairs


import sys


n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
a = map(int,raw_input().strip().split(' '))
count = 0
for x in range(n):
    for y in range(x+1,len(a)):
        if ((a[x]+a[y])%k)==0:
            count = count + 1
print count 
