class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
class Tree:
    node= None
    def insert(self,arr,start,end):
        if start>end:
            return None
        mid = (start+end)/2
        node = Node(arr[mid])
        node.left = self.insert(arr,start,mid-1)
        node.right = self.insert(arr,mid+1,end)            
        return node
    def traverseInOrder(self, root):
        """
        traverse function will print all the node in the tree.
        """
        if root is not None:
            
            self.traverseInOrder(root.left)
            print root.data
            self.traverseInOrder(root.right)

tree = Tree()
arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
root_ = tree.insert(arr, 0, n - 1);
tree.traverseInOrder(root_)    
