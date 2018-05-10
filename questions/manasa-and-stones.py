#time 1.15hour
#https://www.hackerrank.com/challenges/manasa-and-stones/copy-from/33757941
# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
test_case = int(raw_input())
for _ in xrange(test_case):
    n = int(raw_input())
    a = int(raw_input())
    b = int(raw_input())
    output = []
    output.append((n-1)*a)
    output.append((n-1)*b)
    for x in range(1,n-1):
        output.append(x*a+(n-1-x)*b)
    output = set(output)
    for x in sorted(output):
        print x,
    print 
