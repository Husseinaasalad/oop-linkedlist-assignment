class Node:
    def __init__(self, data):
        self.data = data
        self.next = None# node.py
class Node:
    """Represents a single node in a linked list."""
    def __init__(self, data):
        self.data = data      
        self.next = None      


from node import Node

class LinkedList:
    """A simple singly linked list implementation."""
    def __init__(self):
        self.head = None   

    def append(self, data):
        """Add a new node with the given data at the end of the list."""
        new_node = Node(data)
        
        if not self.head:         
            self.head = new_node
            return
            
        current = self.head
        while current.next:
            current = current.next
            
        current.next = new_node

    def display(self):
        """Print all elements in the linked list."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def search(self, data):
        """Search for a value in the linked list. Returns True if found."""
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False


# demo.py - For testing and Part 2
from node import Node
from linked_list import LinkedList

# Part 2: Basic OOP Practice - Manual nodes
print("=== Part 2: Manual Nodes ===")
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

# Link them
node1.next = node2
node2.next = node3

# Traverse and print
current = node1
while current:
    print(current.data)
    current = current.next

print("\n=== Part 3: LinkedList Class Demo ===")
ll = LinkedList()
ll.append(5)
ll.append(15)
ll.append(25)
ll.append(35)

ll.display()

print("Search for 15:", ll.search(15))
print("Search for 99:", ll.search(99))