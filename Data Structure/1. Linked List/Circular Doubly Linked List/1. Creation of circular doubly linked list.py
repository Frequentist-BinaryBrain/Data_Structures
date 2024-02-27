# Define a Node class to represent a node in the linked list
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None  # Pointer to the next node in the list
        self.prev = None  # Pointer to the previous node in the list

# Define a CircularDoublyLinkedList class
class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None  # Points to the first node in the list
        self.tail = None  # Points to the last node in the list

    # Define the __iter__ method to make the linked list iterable
    def __iter__(self):
        node = self.head  # Start from the head of the list
        while node:
            yield node  # Yield the current node
            node = node.next  # Move to the next node
            # Check if we have reached the end of the circular list
            if node == self.tail.next:
                break  # If so, break the loop to prevent an infinite loop

    #  In the context of your circular doubly linked list code, the yield statement is used within the __iter__ method to produce each node
    #  in the linked list as part of the iteration process. It allows you to iterate over the elements of the list one at a time without
    #  having to store the entire list in memory

    # Method to create a Circular Doubly Linked List with a given node value
    def createCDLL(self, nodeValue):
        newNode = Node(nodeValue)  # Create a new node with the given value
        self.head = newNode  # Set the head of the list to the new node
        self.tail = newNode  # Set the tail of the list to the new node
        newNode.prev = newNode  # Set the previous pointer of the new node to itself
        newNode.next = newNode  # Set the next pointer of the new node to itself
        return 'The CDLL is created successfully'


circularDLL = CircularDoublyLinkedList()
print(circularDLL.createCDLL(5))
print(circularDLL)
print([node.value for node in circularDLL])


