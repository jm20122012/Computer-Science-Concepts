# This class shows how to implement a custom linked list, also containing methods to insert data into the linked list
# in ascending order.
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

        
    def append(self, new_node):
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

            
    def prepend(self, new_node):
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

            
    def insert_after(self, current_node, new_node):
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        elif current_node is self.tail:  # If the current node is also the tail node, set tail.next to be the new node
            self.tail.next = new_node    # and update tail to be the new node
            self.tail = new_node
        else:
            new_node.next = current_node.next   # Point the new node.next at 
            current_node.next = new_node
            
            
    # TODO: Write insert_in_ascending_order() method
    def insert_in_ascending_order(self, new_node):
        # Handle case where no head and no tail, meaning first insert
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            return
            
            
        # First check for case if new node data is less than head data, in which case prepend
        if new_node.data < self.head.data:
            #print(f"Prepending list with new node data <{new_node.data}>")
            self.prepend(new_node)
            return 
        
        
        # Check to see if new node data is greater than tail data, in which case append
        elif new_node.data > self.tail.data:
            #print(f"Appending list with new node data <{new_node.data}")
            self.append(new_node)
            return
            
            
        # Next go through the list and see if the new node data is less than the next nodes data
        # If it is, insert the new node after the current node
        else:
            current_node = self.head
            while True:   
                if current_node is self.tail:
                    break
                    
                if new_node.data < current_node.next.data:
                    #print(f"Inserting new node data <{new_node.data}> after current node data <{current_node.data}")
                    self.insert_after(current_node, new_node)
                    break
                current_node = current_node.next
                

    def remove_after(self, current_node):
        # Special case, remove head
        if (current_node == None) and (self.head != None):
            succeeding_node = self.head.next
            self.head = succeeding_node  
            if succeeding_node == None: # Remove last item
                self.tail = None
        elif current_node.next != None:
            succeeding_node = current_node.next.next
            current_node.next = succeeding_node
            if succeeding_node == None: # Remove tail
                self.tail = current_node

                
    def print_list(self):
        cur_node = self.head
        while cur_node != None: # When cur node reaches the tail, tail.next should be None, causing loop to stop
            cur_node.print_node_data()
            print(end=' ')
            cur_node = cur_node.next
