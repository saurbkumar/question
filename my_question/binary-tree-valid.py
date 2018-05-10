# Python program to check if a binary tree is bst or not
 
INT_MAX = int('inf')
INT_MIN = -int('inf')
class Node:
 
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None
 
 
def isBST(node):
    return (isBSTUtil(node, INT_MIN, INT_MAX))

def isBSTUtil(node, mini, maxi):
    if node is None:
        return True
    if node.data < mini or node.data > maxi:
        return False
    return (isBSTUtil(node.left, mini, node.data -1) and
          isBSTUtil(node.right, node.data+1, maxi))
 

if (isBST(root)):
    print "Is BST"
else:
    print "Not a BST"
