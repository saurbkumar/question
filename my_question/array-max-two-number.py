
# 
# array last n element contain the n max element 
# its a modified bubble sort that terminate early
# for top n min number --> just change the greater sign at line 12 to less
a = [1,4,32,9,800,45,5,6,2]
counter = 0
number = 2
for index,_ in enumerate(a):
    if counter==number:
        break
    for index1,_ in enumerate(a[index+1:]):
        if a[index1]> a[index1+1]:
            # Swap
            a[index1],a[index1+1] = a[index1+1],a[index1]
    counter = counter + 1
