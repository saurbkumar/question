# https://leetcode.com/problems/minimum-size-subarray-sum/

'''
Idea is iterate over the array and keep track of the max number achived so far and if max is negative then make it zero
'''

left = 0
right = 0
minLen = len(nums) + 1
currentSum = 0
while right < len(nums):
while (currentSum < s and right <len(nums)): 
    currentSum = currentSum + nums[right] 
    right = right + 1
minLen = min(minLen, right-left + 1)
while (currentSum >= s and left < right):
    currentSum = currentSum - nums[left]
    left = left + 1
minLen = min(minLen, right-left + 1)

return(0 if minLen == len(nums)+1 else minLen)
