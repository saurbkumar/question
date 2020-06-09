'''
if element not present, right or left will give the nearest index to the element
'''
arr = [3, 6, 9, 12, 15, 17, 19]
n = len(arr)
target = 9
left = 0
right = n - 1

while left < right:
    mid = (left + right) // 2
    if arr[mid] <= target:
        left = mid + 1
    elif arr[mid] > target:
        right = mid - 1

print(right, left)
