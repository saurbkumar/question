'''
https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.

Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None        
root = Node(4)
root.left = Node(9)
root.left.left = Node(5)
root.left.right = Node(1)
root.right = Node(0)


result = [] # that wil store all the path
def findPath(root,path):
    if root.left == None or root.right == None:
        path.append(root.data)
        temp = int("".join(map(str,path)))# convert array on integer in to integer
        global result
        result.append(temp)
        #print(temp)
        return  
    findPath(root.left,path + [root.data])
    findPath(root.right,path+[root.data])
    if path:
        path.pop()

findPath(root,[])
print sum(result)
