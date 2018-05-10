# https://leetcode.com/problems/search-a-2d-matrix/description/
'''
O(log(m) + log(n))
'''
a = [1,2,4,6,7,10,14]

start = 0
end = len(a)-1
target = 7
mid = (start+end)/2
#def binarySearch(a,target)
while(True):
    if start>end:
        break
    if a[mid]==target:
        print(mid)
        break
    elif target > a[mid]:
        start = mid+1
        end = end
    else:
        start = start
        end = mid-1
    mid = (start+end)/2
    
a = [1,2,4,6,7,10,14]


#def binarySearch(a,target)
def getInbetween(arr,target):
    '''
    it will give the index of the element where the target element can be insert
    '''
    start = 0
    end = len(arr)-1
    mid = (start+end)/2
    index = None
    while(True):
        if start>end:
            break
        if (arr[mid]<target and arr[mid+1]>target) or (arr[mid]>target and arr[mid-1]<target):
            index = mid
            print(mid)
            break
        elif target > arr[mid]:
            start = mid+1
            end = end
        else:
            start = start
            end = mid-1
        mid = (start+end)/2
    return index
