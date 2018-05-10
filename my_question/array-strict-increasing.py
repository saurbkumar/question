'''There is an array contains some non-negative integers.
   Check whether the array is perfect or not. An array is
   called perfect if it is first strictly increasing, then 
   constant and finally strictly decreasing
   a =[ 1, 8, 8, 8, 3, 2] -> Strict Increasing
      [1, 1, 2, 2, 1] ->not
'''
def isStrictIncreasing(arr):
    n = len(arr)-1
    i = 1
    while(arr[i]>arr[i-1] and i<n):
        i = i+ 1
    while(arr[i]==arr[i-1] and i<n):
        i = i + 1
    while(arr[i]<arr[i-1] and i<n):
        i = i+ 1
        
    if i==n:
        print("Yes")
    else:
        print("No")
