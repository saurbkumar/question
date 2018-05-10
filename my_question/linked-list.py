class Node(object):
    """
    Node class to hold data and next pointer
    """
    def __init__(self,data=None,next_node=None):
        self.data = data
        self.next_node = next_node
        
    def get_data(self):
        return self.data
    
    def get_next_node(self):
        return self.next_node
    
    def set_next_node(self,next_):
        self.next_node = next_
    
class LinkedList():
    def __init__(self,head=None):
        self.head = head
        
    def insert(self,data):# appned data always at the start
        new_node = Node(data)
        new_node.set_next_node(self.head)
        self.head = new_node
        
    def appendLeft(self,data):
        """ 
        Append left or insert both are same
        """
        self.insert(data)
        
    def length(self):
        counter = 0
        currnet_node = self.head
        while currnet_node:
            currnet_node = currnet_node.get_next_node()
            counter = counter + 1
        return counter
    def appendRight(self,data):
        current = self.head
        for _ in range(self.length()-1): 
            current = current.get_next_node()
        new_node = Node(data) # new node created
        current.set_next_node(new_node)
            
    def search(self, data):
       current = self.head
       found = False
       while (current and found) is False: # loop terminate if either of false
           if current.get_data() == data:
               found = True
           else:
               current = current.get_next_node()
           if current is None:
               raise ValueError("Data Not found")
       return current
   
    def getAll(self):
        """
        Print all the available nodes
        """
        current = self.head
        while current:
          print current.get_data()
          current = current.get_next_node()
          
    def delete(self, data):
        """
        kind of search functionality, where ever find the data, beak the 
        link of current one to the next one
        """
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next_node()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next_node()
        else:
            previous.set_next_node(current.get_next_node())
        
                
                
if __name__ == "__main__":   
    List = LinkedList()
    List.insert(10)
    List.appendRight(20)
    List.appendRight(330)
    List.appendRight(2033)
    List.getAll()
    #List.delete(330)
    print "  "
    #print List.length()
    List = LinkedList()
    List.appendLeft(10)
    List.appendLeft(20)
    List.appendLeft(330)
    List.appendLeft(2033)
    List.getAll()
