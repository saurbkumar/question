"""

Lock #1 to #N and key #1 to #N. Locks have 2 states: locked and unlocked. One key can change the state of one lock if the key label is able to divide the lock label. Ex, key #5 can unlock a locked lock with #25. However, key #2 won't unlock the locked lock #25.

Initally all locks are locked. We try every key on every lock, and how many locks will end up unlocked?
locks = [>1, #2, #3, >4, #5, #6]
keys = [1,2,3,4,5]

Ans: 2
Idea: for every integer, divisors exist in pair except for perfect square:
EX: 
1 -> (1)
2 -> (1,2)
1 -> (1,3)
1 -> (1,4),(2) -> perfect square
So , whether to search for lock going to open or not , it is more efficent to search whether the given number is perfect square or not
as if it perfect square, then only the locak state going to be changed (odd number of divisor)

Lock #8

(1, 8), (2, 4)

Lock #16
()

"""

Test case: N = 4
Walk through the example

def perfect_sqr(N):
    count = 1
    for index in range(2,N+1):
        if index*index <= N:
            count = count + 1
        else:
            break
    return count
    
    
def num_unlocked(N):
    perfct_count = perfect_sqr(N)
