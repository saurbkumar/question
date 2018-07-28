# https://www.geeksforgeeks.org/next-greater-element/

a = [8,2,7,5,1,3]
#a = [4,5,2,25]
stack = []

stack.append(a[0])

for next_ in range(1,len(a)-1):
    if len(a)==0:
        pass
    else:
        element = stack.pop()
        if element <a[next_]:
            stack.append(a[next_])
            print('for {} next greater is {}'.format(element,a[next_]))
        else:
            stack.append(element)
            stack.append(a[next_])
if len(a)!=0:
    for data in stack:
        print("For {} next greater is {}".format(data,-1))        
