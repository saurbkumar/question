'''
Input: [1,2,3]
     4
   /   \
  2     7
 / \   / \
1   3 6   9

Output:
     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None        
root = Node(4)
root.left = Node(2)
root.left.left = Node(1)
root.left.right = Node(3)
root.right = Node(7)
root.right.left = Node(6)
root.right.right = Node(9)

import copy
def reverse(root):
    if root==None:
        return
    temp = copy.deepcopy(root)
    root.left = temp.right
    root.right = temp.left
    reverse(temp.left)
    reverse(temp.right)
reverse(root)
