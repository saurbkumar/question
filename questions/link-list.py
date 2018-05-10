# binary tree data structure

class Node:
    # Node data structure to sore Node key value, node next reference
    def __init__(self,node_value):
        self.value = node_value
        self.next = None
    def getNodeValue(self):
        return self.value
    def getNextNodeValue(self):
        return self.next
    def setNextNodeValue(self,value):
        self.next = value
    def setNewNodeValue(self,value):
        self.value = value
# Note that list not going to contain any node, it just link the head to the node
class UnorderList:
    # in begning when list initialized there will be no node
    def __init__(self):
        self.head = None
        self.list_size = 0
    
    # tocheck whether the list is empty or not 
    def isEmpty(self):
        return self.head == None
    # add nodes in the list
    
    def add(self,value):
        temp = Node(value) # node object created i.e. one node having given value
        # below two lines are to link the node with the list
        temp.setNextNodeValue(self.head)#passig the list head value to next value fo node
        self.head = temp # setting the current node instance to the head of the list # here are more detail https://interactivepython.org/courselib/static/pythonds/BasicDS/ImplementinganUnorderedListLinkedLists.html?highlight=linked%20list#fig-addtohead
    
    #find number of nodes attached to list 
    def size(self):
        count = 0
        currentNode = self.head # as head of the list has the current node instance
        while currentNode != None:
            count = count + 1
            currentNode = currentNode.getNextNodeValue()
        return count
    # to find out the specific element 
    def search(self,value):
        is_available = False
        currentNode = self.head
        while currentNode != None:
            if currentNode.getNodeValue() == value:
                is_available = True
                break
            currentNode = currentNode.getNextNodeValue()
        return is_available
    #remove element for the node list
    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
    
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
    
    def append(self,value):
        pass
    def pop(self):
        pass
    def insert(self,value):
        pass
    def index(self,value):
        pass
mylist = UnorderList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(mylist.size())
print(mylist.search(93))
print(mylist.search(100))
