from node import Node

class LinkedList:
    """Simple Singly Linked List Implementation"""
    
    def __init__(self):
        self.head = None   # Points to the first node

    def append(self, data):
        """Add a new node at the end of the list"""
        new_node = Node(data)
        
        # If list is empty
        if self.head is None:
            self.head = new_node
            return
        
        # Traverse to the last node
        current = self.head
        while current.next is not None:
            current = current.next
        
        # Link the new node at the end
        current.next = new_node

    def display(self):
        """Print the entire linked list"""
        if self.head is None:
            print("List is empty")
            return
            
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def search(self, data):
        """Search for data in the linked list. Returns True if found, else False"""
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False