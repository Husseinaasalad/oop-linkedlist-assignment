# oop-linkedlist-assignment
1. What is the purpose of a class within a linked list?
The Node class will be used as a template for the construction of a node (data+next). At the same time, the LinkedList class will control the chain of nodes.

2. How does a node differ from a linked list?
Node: A single item with data and a pointer to the next node.
LinkedList: An entire data structure consisting of the head node and operations with a chain of nodes.

3. Why is none used in next?
This term indicates the end of the list. This is very convenient when using loops for traversal of elements in order to avoid mistakes when working with the next node of the last one.

4. In what ways does a linked list differ from a Python list?
A Python list occupies contiguous memory space (indexing is faster), whereas a linked list occupies non-contiguous memory space with pointers connecting one node to another. A linked list performs better when inserting and deleting elements.

5. What are the advantages of using OOP for data structures?
Using OOP for data structures results in clean code that is easy to understand and modify.
