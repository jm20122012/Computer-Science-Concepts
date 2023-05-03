from PlaneList import PlaneList

# Plane list is a linked list.  Push will add item to the tail, and pop will grab head.
class PlaneQueue:
    def __init__(self):
        self.plane_list: object = PlaneList()
        self.length: int = 0
    
    #       Write push() and pop() instance methods. push() adds an item to the queue
    #       and adds 1 to length. pop() removes and returns the first item in 
    #       the queue and subtracts 1 from length.
    
    
    def pop(self):
        # Need to return the data of the head node.  For time being, explicitly save data to new variable
        # just to make it clear what is happening
        # print(f"Saving the flight code stored in the current head of PlaneList.  Data: {self.plane_list.head.flight_code}")
        self.head_data = self.plane_list.head.flight_code
        
        # Need to set the second item in the list as the new head
        # print(f"Setting second item as the new head")
        # print(f"Head: {self.plane_list.head}, Next Item: {self.plane_list.head.next}")
        self.plane_list.head = self.plane_list.head.next
        
        # print(f"New head: {self.plane_list.head}")
        
        # Also decrement the self.length counter
        # print("Decrementing plane list length...")
        self.length -= 1
        # print(f"New plane list length: {self.length}")
                
        return self.head_data    
    
    def push(self, node):
        # Add plane flight code to end of list
        # print(f"Adding plane to queue...")
        # print(f"Current tail: {self.plane_list.tail} - New tail: {node}")
        self.plane_list.append(node)
        
        # print(f"New tail: {self.plane_list.tail}")
        
        # Increment plane list length
        # print("Incrementing plane list length")
        self.length += 1
        
        # print(f"New length: {self.length}")

    def is_empty(self):
        return self.length == 0
        
    def print_queue(self):
        print('Air-traffic control queue')
        if not self.is_empty():
            print('   Next to land:', end=' ')
            cur_node = self.plane_list.head
            cur_node.print_node_data()
            print()
            
            if self.length > 1:
                print('   Arriving flights:')
                cur_node = cur_node.next
                while cur_node is not None:
                    print('      ', end='')
                    cur_node.print_node_data()
                    print()
                    cur_node = cur_node.next
        else:
            print('Queue is empty.')
        print()
        
if __name__ == "__main__":
    import PlaneNode
    new_queue = PlaneQueue()
    
    print(f"{30 * '-'} Creating new nodes {30 * '-'}")
    plane1 = PlaneNode.PlaneNode(flight_code="Flight123")
    plane2 = PlaneNode.PlaneNode(flight_code="Flight456")
    
    print(f"{30 * '-'} Pushing new nodes to queue {30 * '-'}")
    new_queue.push(plane1)
    new_queue.push(plane2)
    
    print(f"{30 * '-'} Poping last item in queue list {30 * '-'}")
    landed_flight_code = new_queue.pop()
    print(f"Flight code of popped flight: {landed_flight_code}")
    
