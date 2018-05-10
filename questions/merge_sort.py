def merge(alist,lefthalf,righthalf,i,j,k):
    # comparing the element in two list
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1
        # comping the element form lefthalf
        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1
        # copying the element in righthalf
        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
            
def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=0
        j=0
        k=0
        merge(alist,lefthalf,righthalf,i,j,k)
            
        
alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)
