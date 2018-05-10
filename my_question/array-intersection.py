'''
Gives the unique element in the two set
'''
a = [1,2,3,4,5,8,10,13,17]
b = [1,3,5,9,10,199]
len_a = len(a)
len_b = len(b)
index_a = 0
index_b = 0
while (True):
    # index upper limit reached
    if index_a>=len_a-1 or index_b>=len_b-1:
        break
    #
    if a[index_a]<b[index_b]:
        index_a = index_a + 1
    if a[index_a]>b[index_b]:
        index_b = index_b + 1
    if a[index_a]==b[index_b]:
        print a[index_a]
        index_b = index_b + 1
        index_a = index_a + 1
