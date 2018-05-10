'''
Input:  arr[] = [[1,3], [5,7], [2,4], [6,8]]
Output: true
Reason :The intervals [1,3] and [2,4] overlap
'''
'''
1. sort the array on the basis of the first element.
2. Iterate over the sorted array , if the first element of the current (i.e)
item is smaller then the last element of the previous item, then 
there is over lap
https://www.geeksforgeeks.org/merging-intervals/
'''
data = [[1,3], [5,7], [17,58]]
from collections import defaultdict

table = defaultdict(list)

for element in data:
	table[element[0]].append(element)
process_data = []	
# for sorting
first_elemts = sorted(table.keys())
for elem in first_elemts:
	process_data.extend(table[elem])
	
# for second condition check
for index in range(1,len(process_data)):
	if (process_data[index-1][1] > process_data[index][0]):
		print' yes there is overlap'
		break

'''
Input:  =  [[1,3], [5,7], [2,4], [6,8],[1,9]]
output : [1,9]

'''
data = [[1,3], [5,7], [2,4], [6,8],[2,9]]
from collections import defaultdict

table = defaultdict(list)

for element in data:
	table[element[0]].append(element)
process_data = []	
# for sorting
first_elemts = sorted(table.keys())
for elem in first_elemts:
	process_data.extend(table[elem])
# initilize the range
previous_range = process_data[0]
for index in range(1,len(process_data)):
	if (process_data[index-1][1] > process_data[index][0]):
		# interval overlap, update the interval -> previous_range
		#prev = process_data[index-1]
		curr = process_data[index]
		new_start = min(previous_range[0],curr[0])# starting point of the range
		new_end = max(previous_range[1],curr[1])# ending point of the range
        # update the range
		previous_range = [new_start,new_end]
print(previous_range)
