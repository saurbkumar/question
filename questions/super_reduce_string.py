#https://www.hackerrank.com/challenges/reduced-string

from __future__ import print_function
string = raw_input()
stack = []
for letter in string:
    if len(stack) ==0:
        stack.insert(0,letter)
    elif letter==stack[0]:
        stack.pop(0)
    else:
        stack.insert(0,letter)
if len(stack)==0:
    print ("Empty String")
else:
    for i in range(-1,-len(stack)-1,-1):
        print(stack[i],end='')
