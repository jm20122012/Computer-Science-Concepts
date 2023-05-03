# This program uses the "LinkedList" and "Node" class to implement a Linked List data type.  This program takes an array 
# and inserts each element in the array into the linked list in ascending order.
import LinkedList
import Node

linked_list = LinkedList()
arr = [4, 3, 12, 2, 5, 4, 8, 5, 3, 8, 6, 8, 9, 10, 11, 13, 4, 3, 6]
for i in arr:
    print(30 * '-')
    print(f"Creating new node with value {i}")
    new_node = Node(i)
    linked_list.insert_in_ascending_order(new_node)
linked_list.print_list()
