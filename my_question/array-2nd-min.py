
1) Initialize both first and second smallest as INT_MAX
   first = second = INT_MAX
2) Loop through all the elements.
   a) If the current element is smaller than first, then update first 
       and second. 
   b) Else if the current element is smaller than second then update 
    second
    
    import sys
 
def print2Smallest(arr):
 
    # There should be atleast two elements
    arr_size = len(arr)
    if arr_size < 2:
        print "Invalid Input"
        return
 
    first = second = sys.maxint
    for i in range(0, arr_size):
 
        # If current element is smaller than first then
        # update both first and second
        if arr[i] < first:
            second = first
            first = arr[i]
 
        # If arr[i] is in between first and second then
        # update second
        elif (arr[i] < second and arr[i] != first):
            second = arr[i];
 
    if (second == sys.maxint):
        print "No second smallest element"
    else:
        print 'The smallest element is',first,'and' \
              ' second smallest element is',second
 
# Driver function to test above function
arr = [12, 13, 1, 10, 34, 1]
print2Smallest(arr)

