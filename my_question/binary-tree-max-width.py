#https://leetcode.com/problems/maximum-width-of-binary-tree/discuss/
#http://massivealgorithms.blogspot.com/2017/08/leetcode-662-maximum-width-of-binary.html
class Node:
    def __init__(self ,key):
        self.data = key
        self.left = None
        self.right = None
def widthOfBinaryTree( root):
    # initilize the root
    queue = [(root, 0, 0)]
    cur_depth = left = ans = 0
    #iterate over the queue
    # appending will stop when the next node is none
    for node, depth, pos in queue:
        if node:
            # Assign the left and right node, even if doesn't exist
            # reason 
            '''
            Even the X node doesn't exist but appeneded as to increase the position 
            counter
            
                        1
                   2         3
                 4   5     6   7
                8 9 x 11  x 13 x 15
            '''
            queue.append((node.left, depth+1, pos*2))
            queue.append((node.right, depth+1, pos*2 + 1))
            # this will run only once when the depth changed
            if cur_depth != depth:
                cur_depth = depth
                # this is to make sure the case whent the left most node is
                # missing, if the below line comment out, then the left most 
                # is always zero
                '''
                Below assignment for the case like this. in this case, left is
                zero, but in actual it is 1
                #                2
                #           /         \
                #          3           5  
                #           \         / \ 
                #            12      3   45

                '''
                left = pos
            ans = max(pos - left + 1, ans)

    return ans
root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(12)
root.right.left = Node(13)

root.left.left.right = Node(18)
root.right.left.right = Node(33)

print(widthOfBinaryTree(root))
