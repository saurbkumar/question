'''
Input: "00110011"
Output: 6

Reason: 6 substrings, with equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
'''

'''
Method one - Iterate over the sting and keep a track of the current element and 
the previous, along with the zero and one count. Reset the counter when ever
change occours
'''
data = '00110011'
count = [0,0]
pattern = 0
previous= None
for index,elem in enumerate(data):
    current = elem
    if current==previous:
        if next_elme in not == current:
            pattern = pattern + min(count)
            if current==0:
                count[1]=0
            else:
                count[0]=0
        else:
            if current=='0':
                count[0] = count[0]+1
            else:
                count[1] = count[1]+1
    else:
        if current=='0':
            count[0] = count[0]+1
        else:
            count[1] = count[1]+1
'''
Problem with above is lots of corner case missed and bit difficult to visualized
what going on
'''

####### other way ####### 
'''
calculate the number of the repetation of the zeros and one like
110001111000000 - > [2, 3, 4, 6]
then find the min of curretn elemtn with the previous elemnt and add it to 
counter
'''
repetation = []
data = "110001111000000"
counter = 1
pattern = 0
for index in range(1,len(data)):
    if data[index-1]==data[index]:
        counter = counter + 1
    else:
        repetation.append(counter)
        counter = 1
repetation.append(counter)
# repetation will have - > [2, 3, 4, 6]
for index in range(1,len(repetation)):
    pattern = pattern + min (repetation[index],repetation[index-1])





