http://www.geeksforgeeks.org/level-order-tree-traversal/
class Node:
    def __init__(self ,key):
        self.data = key
        self.left = None
        self.right = None
def printLevelOrder(root):
    '''
    when want output in the 
    1 2 3 4 5
    '''
    if root is None:
        return
    queue = []
    queue.append(root)
    while(queue):
        print queue[0].data,
        node = queue.pop(0)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
def printLevelOrder1(root):
    '''
    When want output in 
    1
    2 3 
    4 5
    '''
    if root is None:
        return
    queue = []
    queue.append(root)
    while(queue):
        for node in queue:
            print node.data,
        print""
        length = len(queue)
        for i in range(length):
            node = queue.pop(0)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

printLevelOrder(root)
