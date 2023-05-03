class PlaneNode:
    def __init__(self, flight_code='0'):
        self.flight_code: str = flight_code
        self.next: object = None
        
    def print_node_data(self):
        print(self.flight_code, end='')
