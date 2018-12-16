# https://dxmahata.gitbooks.io/leetcode-python-solutions/kth_smallest_element_in_a_bst.html
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
root = Node(100)
root.left = Node(60)
root.right = Node(130)
root.right.right = Node(170)
root.right.left = Node(120)
root.left.left = Node(50)
root.left.right = Node(65)
path = []
result  = None
#
def getLeft(root,k):
    node = root
    stack = []
    count = 0
    while stack!=[] or node!=None:
        if node:
            stack.append(node)
            node = node.left
        else:
            
            temp_node = stack.pop()
            count = count + 1
            if count==k:
                return temp_node
            else:
                  if node:
                    node = node.right
            
    return None
data = getLeft(root,1)
print(data.data)

# or ------
# K -> kth element looking for, curr- > current ith smallest element
# Idea - tree is binary search, so do the inorder traverse and count the curr position
def kSmall(root,k,curr):
    # root is none, return the curr counter value
    if root==None:
        return curr
    # inorder traversal
    curr = kSmall(root.left,k,curr)
    curr = curr + 1
    if(curr==k):
        print(root.data)
    curr = kSmall(root.right,k,curr)
    return curr
current=0
kSmall(root,7,current)
