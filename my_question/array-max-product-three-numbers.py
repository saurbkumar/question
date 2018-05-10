'''
https://leetcode.com/problems/maximum-product-of-three-numbers
Given an integer array (can contain -ve number also), find three numbers whose 
product is maximum and output the maximum product.

Input: [1,2,3,4]
Output: 24

Input: [1,-26,-3,4]
Output: 312

Idea: Sort the array and then use 
max(arr[0]*arr[1]*arr[-1],arr[-1]*arr[-2],arr[-3])
where arr[-1] is the last element

O(nLogn)

Other way use heap
'''
import heapq
arr = [1,-26,-3,4]

a,b = heapq.nlargest(3,arr), heapq.nsmallest(2,arr)
answer = max(a[0]*a[1]*a[2],a[0]*b[0]*b[1])
