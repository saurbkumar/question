#time - not able to solev 

https://www.hackerrank.com/challenges/beautiful-triplets
# Enter your code here. Read input from STDIN. Print output to STDOUT
n,d = map(int,raw_input().split())
c = map(int,raw_input().split())
count = 0
for i in range(n):
    if c[i]+d in c and c[i]+2*d in c:
        count+=1
print count
