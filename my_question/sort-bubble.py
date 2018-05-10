a = [1,44,32,5,6,2]
for index in range(len(a)):
    for index1  in range(len(a[index+1:])):
        if a[index1]> a[index1+1]:
            # Swap
            a[index1],a[index1+1] = a[index1+1],a[index1]
