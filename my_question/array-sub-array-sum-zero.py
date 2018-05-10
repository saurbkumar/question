'''
consider an array [4, 2, -3, 1, 6, 3], need to find whether it has any sub arrya, whose sume is zero - (element should be continous)
Ex - [2,-3,1] --> sum is zeor, however [-3,3] --> sum is also zero but they are not continous, so this one should not be consider
Strategy - http://www.geeksforgeeks.org/find-if-there-is-a-subarray-with-0-sum/
'''

a = [-3, 2, 3, 1, 6]
isAvailable = "Not"
table = dict()
current_sum = 0
for element in a:
    current_sum = current_sum + element
    try:
        '''
        if current sum is available then zero
        then the zero sum sub arrya is available
        Its a pattern
        '''
        value = table[current_sum]
        if value:
            isAvailable = "Yes"
            break
    except:
        table[current_sum] = True
print isAvailable
