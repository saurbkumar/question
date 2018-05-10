# Python program to find the equilibrium
# index of an array

'''
nums = [1, 7, 3, 6, 5, 6]
Output: 3
Explanation: 
The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
Also, 3 is the first index where this occurs.
'''
def equilibrium(arr):
	total_sum = sum(arr)
	leftsum = 0
	for i, num in enumerate(arr):
		total_sum = total_sum - num
		if leftsum == total_sum:
			return i
		leftsum = leftsum + num
	
	# If no equilibrium index found, 
	# then return -1
	return -1
  
arr = [1,7,3,6,5,6]
print ('First equilibrium index is ',
	equilibrium(arr))
