class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
root = Node(100)
root.left = Node(120)
root.right = Node(130)
root.right.right = Node(170)
root.right.left = Node(160)
root.left.left = Node(140)
root.left.right = Node(150)
path = []
result  = None
def findPath(root,key):
    if root == None:
        return False  
    if root.data == key:
        return [root.data]
    status = findPath(root.left,key)
    if status:
        return [root.data] + status
    status = findPath(root.right,key)
    if status:
        return [root.data] + status
    return []
print(findPath(root,150))
