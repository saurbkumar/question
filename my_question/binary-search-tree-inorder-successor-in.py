# https://www.geeksforgeeks.org/inorder-successor-in-binary-search-tree/

'''
Idea: If target node has right sub-tree, then the smallest element in that is the inorder successor, if node does not has left sub tree
then the immediate parent is the inorder successor

https://youtu.be/JdmAYw5h3G8?t=556
'''

'''
If right subtree exist, then the target is the lowest value in that tree
If right subtree does exist, then start from the root and search for the node that we are searching for the inorder successor,
from the root node, where we have taken the first left to the target node, is node that we are looking for
'''

