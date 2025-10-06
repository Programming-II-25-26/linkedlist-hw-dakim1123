# LinkedLists HW
'''
Problem: Write a function that reverses a LinkedList

Your function should take in the head of a list as a parameter, and retun the head of the reversed linked list 
'''

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
    prev = None
    current = head
    while current != None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev

list = [1, 2, 4, 8, 16, 32, 64, 128]
head = create_list(list)
print_list(head)

head = reverse_list(head)
print_list(head)