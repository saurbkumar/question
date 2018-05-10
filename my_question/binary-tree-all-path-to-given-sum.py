class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
root = Node(100)
root.left = Node(120)
root.right = Node(50)
root.right.right = Node(70)
root.right.left = Node(160)
root.left.left = Node(140)
root.left.right = Node(150)
path = []
result  = []
import copy
def findPath(root,key,sum_,path):
    if root == None:
        return
    path.append(root.data)
    if key == sum_+root.data:
        print ("key found",path)
        result.append(copy.deepcopy(path))
        path.pop()
        return
    findPath(root.left,key,sum_ + root.data,path)
    findPath(root.right,key,sum_ + root.data,path)
    path.pop()
findPath(root,220,0,path)
