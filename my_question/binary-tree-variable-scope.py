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

'''
consider a case of finding a path to the node
'''

'''
Here note that, the I am returning the path (which is a list), though it is not necessary, as every recursion will always point
to the same list (path) however with the variables that is not the case
'''
def getpath(root,path,target):
    if(root==None):
        return path
    path.append(root.data)
    if(root.data==target):
        print(path)
        path.pop()
        return path
    path = getpath(root.left,path,target)
    path = getpath(root.right,path,target)
    path.pop()
    return path
getpath(root,[],160)

'''
the below one is will also work, see I am not returning any path. Here only one instance of the path will create for a 
recursion 
'''

def getpath(root,path,target):
    if(root==None):
        return
    path.append(root.data)
    if(root.data==target):
        print(path)
        path.pop()
        return
    getpath(root.left,path,target)
    getpath(root.right,path,target)
    path.pop()
getpath(root,[],160)

'''
However that is not the case with the variables (variables I mean to say integers but not list), for every recursion a different instance
of the variable (curr) will created and that's why I need to pass K value, If i dont pass the k value, it will take the old values
'''
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


