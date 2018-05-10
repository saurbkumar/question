# http://www.geeksforgeeks.org/how-to-determine-if-a-binary-tree-is-balanced/

class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def depth(root,curr_height):
    if root == None:
        return curr_height
    h1 = height(root.left,curr_height+1)
    h2 = height(root.right,curr_height+1)
    return max(h1,h2)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
left_height = depth(root.left)
right_height = depth(root.right)

if abs(left_height-right_height)==1:
    print("Balance Tree")
else:
    print("Not a Balance Tree")
