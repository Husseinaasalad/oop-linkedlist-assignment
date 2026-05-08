from node import Node
from linked_list import LinkedList

print("=== Part 2: Manual Nodes ===")
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.next = node3

current = node1
while current:
    print(current.data)
    current = current.next

print("\n=== Part 3: LinkedList Class ===")
ll = LinkedList()
ll.append(5)
ll.append(15)
ll.append(25)
ll.append(35)

ll.display()

print("Search 15:", ll.search(15))
print("Search 99:", ll.search(99))