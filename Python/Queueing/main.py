from PlaneQueue import PlaneQueue
from PlaneNode import PlaneNode

if __name__ == "__main__":
    plane_queue = PlaneQueue()
    
    # TODO: Read in arriving flight codes and whether a flight has landed. 
    #       Print the queue after every push() or pop() operation. If the user
    #       entered "landed", print which flight has landed. Continue until -1 
    #       is read.
    
    # Example, if input is:
    # arriving AA213
    # arriving DAL23
    # arriving UA628
    # landed
    # -1
    
    # Output is:
    # Air-traffic control queue
    # Next to land: AA213

    # Air-traffic control queue
    # Next to land: AA213
    # Arriving flights: 
    #     DAL23

    # Air-traffic control queue
    # Next to land: AA213
    # Arriving flights: 
    #     DAL23
    #     UA628

    # AA213 has landed.
    # Air-traffic control queue
    # Next to land: DAL23
    # Arriving flights: 
    #     UA628
    
    while True:
        # Get user input
        user_input = input()
        
        # If user input is -1, string or int, break from the while loop
        if user_input == -1 or user_input == "-1":
            break
        
        # Handle case for adding plane flight codes to queue
        elif user_input.split(" ")[0] == "arriving":
            new_plane = PlaneNode(user_input.split(" ")[1]) # Create new node and pass flight number
            plane_queue.push(new_plane)
            plane_queue.print_queue()
        
        # Handle cases for landed planes, and dequeueing planes from queue
        elif user_input == "landed":
            landed_flight_code = plane_queue.pop()
            print(f"{landed_flight_code} has landed.")
            plane_queue.print_queue()
            
        else:
            print("Invalid input")
        
        
        
