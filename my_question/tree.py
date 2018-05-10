class Node:
    '''
    Node class, it will act as a 
    container for the tree nodes value and
    children position
    '''
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    '''
    That will generate tree,
    '''
    def createNode(self,data):
        '''
        Create node
        '''
        return Node(data)
    def insert(self,node,data):
        if node is None:
            '''
            No root node -> create one
            '''
            return self.createNode(data)
        if node.data>data:
            node.left = self.insert(node.left,data)
        else:
            node.right = self.insert(node.right,data)
            
        return node
    def search(self,node,data):
        if node is None or node.data ==data:
            return node
        if node.data<data:
            return self.search(node.right,data)
        else:
            return self.search(node.left,data)
    def inorder(self,root_node):
        if root_node is  not None:
            self.inorder(root_node.left)
            print(root_node.data)
            self.inorder(root_node.right)
    def traversePreorder(self, root):
        """
        traverse function will print all the node in the tree.
        """
        if root is not None:
            print root.data
            self.traversePreorder(root.left)
            self.traversePreorder(root.right)

    def traversePostorder(self, root):
        """
        traverse function will print all the node in the tree.
        """
        if root is not None:
            self.traversePreorder(root.left)
            self.traversePreorder(root.right)
            print root.data

def main():
    root = None
    tree = Tree()
    root = tree.insert(root, 10)
    print root
    tree.insert(root, 20)
    tree.insert(root, 30)
    tree.insert(root, 40)
    tree.insert(root, 70)
    tree.insert(root, -1)
    tree.insert(root, 80)
    tree.inorder(root)
if __name__ == "__main__":
    main()
