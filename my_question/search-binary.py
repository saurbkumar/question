'''
Binary Search
'''
lst = [1,3,5,7,9,11,13,67]
number = 9000

def binarySearch(lst,number):
    mn = 0
    mx = len(lst)-1
    while True:
        n = (mn+mx)//2
        if mn>mx:
            return -1
        if lst[n]>number:
            mx = n-1
        elif lst[n]<number:
            mn = n+1
        else:
            return n
print binarySearch(lst,number)
