#time - 15 min
#https://www.hackerrank.com/challenges/insertionsort1/submissions/code/35608529
#!/bin/python
def insertionSort(arr):    
    for j in range(1,len(arr)):
        key = ar[j]
        i = j-1
        while i>-1 and arr[i]>key:
            arr[i+1] = arr[i]
            i = i -1
            for a in arr:
                print a,
            print
        arr[i+ 1]=key
    return arr

m = input()
ar = [int(i) for i in raw_input().strip().split()]
aa = insertionSort(ar)
for a in aa:
    print a,

