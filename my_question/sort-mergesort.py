def mergeSort(array):
    if len(array)>1:
        midPoint = len(array)//2
        leftpart = array[:midPoint]
        rightpart = array[midPoint:]
        mergeSort(leftpart)
        mergeSort(rightpart)
        i=0
        j=0
        k=0
        while i < len(leftpart) and j < len(leftpart):
            if leftpart[i] < rightpart[j]:
                array[k]=leftpart[i]
                i=i+1
            else:
                array[k]=rightpart[j]
                j=j+1
            k=k+1
        while i < len(leftpart):
            array[k]=leftpart[i]
            i=i+1
            k=k+1
        while j < len(rightpart):
            array[k]=rightpart[j]
            j=j+1
            k=k+1
    return array
alist = [54,26,93,17,77,31,44,55,20]
print mergeSort(alist)

