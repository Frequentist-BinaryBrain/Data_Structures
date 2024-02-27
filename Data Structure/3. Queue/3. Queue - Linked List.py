# To Create a Queue, first Create an object of Linked List class

# Define a Node class to represent individual elements in the linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

# Define a LinkedList class to manage the linked list structure
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the linked list
        self.tail = None  # Initialize the tail of the linked list

    def __iter__(self):
        curNode = self.head
        # Define an iterator to traverse through the linked list
        while curNode:
            yield curNode  # Yield the current node in the iteration
            curNode = curNode.next  # Move to the next node in the linked list

# Define a Queue class that uses the LinkedList class to implement a queue
class Queue:
    def __init__(self):
        self.linkedList = LinkedList()  # Create a linked list object for the queue

    def __str__(self):
        # Convert the elements of the linked list to a string for display
        values = [str(x) for x in self.linkedList if x is not None]
        return ''.join(values)

    def enqueue(self, value):
        # Enqueue (insert) a new node with the given value into the queue
        newNode = Node(value)

        if self.linkedList.head is None:
            # If the queue is empty, set both head and tail to the new node
            self.linkedList.head = newNode
            self.linkedList.tail = newNode
        else:
            # If the queue is not empty, add the new node to the end of the linked list
            self.linkedList.tail.next = newNode
            self.linkedList.tail = newNode

    def isempty(self):
        # Check if the queue is empty by examining the head of the linked list
        if self.linkedList.head == None:
            return True
        else:
            return False

    def dequeue(self):
        # Check if the queue is empty before attempting to dequeue
        if self.isempty():
            return "No element in the queue to dequeue"
        else:
            # Retrieve the current node at the head of the linked list
            current_node = self.linkedList.head

            # Check if there is only one element in the queue
            if self.linkedList.head == self.linkedList.tail:
                # If yes, set both head and tail to None, indicating an empty queue
                self.linkedList.head = None
                self.linkedList.tail = None
            else:
                # If there are more than one element, move the head to the next node
                self.linkedList.head = self.linkedList.head.next

            # Return the dequeued node
            return current_node

    def peek(self):
        if self.isempty():
            return "There is no element in queue to peek"
        else:
            return self.linkedList.head

    def delete(self):
        self.linkedList.head = None
        self.linkedList.tail = None







