'''
Input : [1, 2, 3, 1]
Output : 2
Reason :3 is a peak element and your function should return the index number 2.
'''
data = [1,2,3,4,5,8,5,4,2,1]
start = 0
end = len(data)-1
condition = True
while condition:
# modified form of binary search, run on paper, it's easy :)
	pivot = (start+end)/2
	# increasing sequ
	if data[pivot-1]<data[pivot] and data[pivot]<data[pivot+1]:
		start = pivot
	# decreasing sequence
	elif data[pivot-1]>data[pivot] and data[pivot]>data[pivot+1]:
		end = pivot
	else:
		condition = False
		print pivot
