#Starter Ccode below including helper functions 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_list(head):
    """Helper function to print your list"""
    current = head
    while current != None:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

def create_list(values):
    """Helper function to create a list from a list of values"""
    if not values:
        return None
    head = Node(values[0])
    current = head
    for value in values[1:]:
        current.next = Node(value)
        current = current.next
    return head

def reverse_list(head):
    # Your code here
    pass
