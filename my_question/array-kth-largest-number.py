

import heapq
# In python by default is min heap
'''
https://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array/
Given an array and a number k where k is smaller than size of array
Input: arr[] = {7, 10, 4, 3, 20, 15}
       k = 3
Output: 7

Input: arr[] = {7, 10, 4, 3, 20, 15}
       k = 4
Output: 10
'''
k = 2# i.e. pop the min element two times
a = [1,3,6,8,9]
heapq.heapify(a)
count = 1
for index in range(k):
    if count==k:
        print heapq.heappop(a)
    else:
        heapq.heappop(a)
    count = count + 1
