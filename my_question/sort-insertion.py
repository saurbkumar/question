def insertionSort(arr):    
    for j in range(1,len(arr)):
        key = arr[j]
        i = j-1
        while i>-1 and arr[i]>key:
            arr[i+1] = arr[i]
            i = i -1
        arr[i+ 1]=key
    return arr
print insertionSort([1,22,11,345,12])
