# Lowest Common Ancestor in binary search tree
# More detail here  - http://www.geeksforgeeks.org/lowest-common-ancestor-in-a-binary-search-tree/
# https://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/

# Here idea is to find the that node, which is in between the value of the given two leaf node (or any node)

 # When tree is binary search tree
def lca(root, n1, n2):
    if root is None:
        return None
    # If both n1 and n2 are smaller than root, then LCA lies in left
    if(root.data > n1 and root.data > n2):
        return lca(root.left, n1, n2)
    # If both n1 and n2 are greater than root, then LCA lies in right 
    if(root.data < n1 and root.data < n2):
        return lca(root.right, n1, n2)
    return root
    
    
 # When tree is not binary search tree
 
# So the only option is to find out the path from source to two target nodes and store those paths in to an array.

# now iterate over both arrays where the last mismatch occour in the arrays, the common element is the 1-lastmismatch location

def searchPath( root, path, k):
 
    # Baes Case
    if root is None:
        return False
    path.append(root.key)
 
    # See if the k is same as root's key
    if root.key == k :
        return True
 # Below is important as it is tree traversal --> IMPORTANT
 # Check if k is found in left or right sub-tree
    if ((root.left != None and searchPath(root.left, path, k)) or (root.right!= None and searchPath(root.right, path, k))):
        return True      
    path.pop()
    return False

   
# other way - Basic assumption , keys are available in the tree
# advantage of this - only one tree traversal without extra storage

class Node:
	    def __init__(self, key):
	        self.key = key 
	        self.left = None
	        self.right = None
def findLCA(root, n1, n2):
	    if root is None:
	        return None
	    if root.key == n1 or root.key == n2:
	        return root 
	    left_lca = findLCA(root.left, n1, n2) 
	    right_lca = findLCA(root.right, n1, n2)
	    if left_lca and right_lca:
	        return root 
	    return left_lca if left_lca is not None else right_lca
	
root = Node(80)
root.left = Node(90)
root.left.left = Node(50)
root.left.right = Node(60)
root.left.left.left = Node(70)
root.left.left.right = Node(2)
print "LCA(4,5) = ", findLCA(root, 70, 60).key
