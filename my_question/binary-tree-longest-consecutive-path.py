'''
       10
      /    \     
     /      \
    11        9	
   / \        /\
  /   \      /  \
13    12    13   8
Maximum Consecutive Path Length is 3 (10, 11, 12)
Note: 10, 9 ,8 is NOT considered since
the nodes should be in increasing order.

	    5
          /  \
         /    \
        8      11
        /        \
       /          \
       9	  10   
      /	          /
     /	         /
    6           15
Maximum Consecutive Path Length is 2 (8, 9).
'''
http://www.geeksforgeeks.org/maximum-consecutive-increasing-path-length-in-binary-tree/
# for same numbers sequence - just remove +1 from 13 and 14
class Node:
    def __init__(self, val):
        self.val = val 
        self.left = None
        self.right = None
def maxPathLenUtil(root, prev_val, prev_len):
    if root is None:
        return prev_len 
    curr_val =  root.val
    if curr_val == prev_val +1 :
        return max(maxPathLenUtil(root.left, curr_val, prev_len+1), 
                   maxPathLenUtil(root.right, curr_val, prev_len+1))
 
    newPathLen = max(maxPathLenUtil(root.left, curr_val, 1),
                    maxPathLenUtil(root.right, curr_val, 1))
    return max(prev_len , newPathLen)
 

def maxConsecutivePathLength(root):
    if root is None:
        return 0
    return maxPathLenUtil(root, root.val -1 , 0)

root = Node(10)
root.left = Node(11)
root.left.left = Node(1)
root.left.left.left = Node(2)
root.left.left.left.left = Node(3)

print maxConsecutivePathLength(root)
