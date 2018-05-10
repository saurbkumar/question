class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.right = None
start = Node(10)
start.right = Node(20)
start.right.right = Node(30)
start.right.right.right = Node(40)
head = None
def reverse(curr_node,prev_node):
    if curr_node == None:
        global head
        head = prev_node# ro the better way is to use class as done here https://www.geeksforgeeks.org/reverse-a-linked-list/
        return 
    next_ = curr_node.right
    curr_node.right = prev_node
    prev_node = curr_node
    reverse(next_,prev_node)
    
