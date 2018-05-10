#time - 15 min 
#https://www.hackerrank.com/challenges/equality-in-a-array



# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
n = input()
a = map(int,raw_input().split())
b = Counter(a)
repetation = b.values()
min_number = sum(repetation) - max(repetation) 
print min_number
