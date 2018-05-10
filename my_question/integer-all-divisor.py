# https://www.geeksforgeeks.org/find-divisors-natural-number-set-1/
import math
def printDivisors(n) :
    i = 1
    while i <= math.sqrt(n) + 1 :
        if (n % i == 0) :
            # If divisors are equal, print only one
            if (n / i == i) :
                print i,
            else :
                # Otherwise print both
                print i , n/i,
        i = i + 1
printDivisors(100)
# in sorted way
# A O(sqrt(n)) java program that prints 
# all divisors in sorted order
import math 
 
# Method to print the divisors
def printDivisors(n) :
    list = [] 
     
    # List to store half of the divisors
    for i in range(1, int(math.sqrt(n) + 1)) :
         
        if (n % i == 0) :
             
            # Check if divisors are equal
            if (n / i == i) :
                print (i, end=" ")
            else :
                # Otherwise print both
                print (i, end=" ")
                list.append(int(n / i))
                 
    # The list will be printed in reverse    
    for i in list[::-1] :
        print (i, end=" ")
