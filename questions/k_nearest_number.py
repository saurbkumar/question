# find the K number that is lees then to given number in the sorted array 

def binary_search(array, target):
    """
    This program will return the index of the queryed number, if element is
    not available then it will return the index of the element of that is
    just less then to the element
    """
    lower = 0
    upper = len(array)
    while lower < upper:   # use < instead of <=
        x = lower + (upper - lower) // 2
        val = array[x]
        if target == val:
            return x
        elif target > val:
            if lower == x:   # this two are the actual lines
                break        # you're looking for
            lower = x
        elif target < val:
            upper = x
    return x
            
            

number = 67
length = 4
a = [1,2,44,55,66,78,89]
#with loops - linear search            
for i in range(len(a)):
    if number<=a[i]:
        break
# with binary search
i = binary_search(a,number)    
print a[i-length:i]