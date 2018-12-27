# https://www.geeksforgeeks.org/find-subarray-with-given-sum/

for index in range(1,len(arr)):
    # add current number to the sum
    curr_sum = curr_sum + arr[index]
    if curr_sum==target_sum:
        print("targer found",start,index)
    # if curr sume id greater then subtract the initial number till  start point
    # is greater to the index and currSum > target
    if curr_sum>target_sum:
        while curr_sum>target_sum and start<index:
            curr_sum = curr_sum -arr[start]
            start = start + 1
            if curr_sum==target_sum:
                print("targer found inner",start,index)
