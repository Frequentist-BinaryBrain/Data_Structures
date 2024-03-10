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

    def enqueue(self, value):
        # Enqueue (insert) a new node with the given value into the queue
        newNode = Node(value)

        if self.head is None:
            # If the queue is empty, set both head and tail to the new node
            self.head = newNode
            self.tail = newNode
        else:
            # If the queue is not empty, add the new node to the end of the linked list
            self.tail.next = newNode
            self.tail = newNode

    def isempty(self):
        # Check if the queue is empty by examining the head of the linked list
        return self.head is None

    def dequeue(self):
        # Check if the queue is empty before attempting to dequeue
        if self.isempty():
            return None
        else:
            # Retrieve the current node at the head of the linked list
            current_node = self.head

            # Check if there is only one element in the queue
            if self.head == self.tail:
                # If yes, set both head and tail to None, indicating an empty queue
                self.head = None
                self.tail = None
            else:
                # If there are more than one element, move the head to the next node
                self.head = self.head.next

            # Return the dequeued node
            return current_node


# Define a Queue class that uses the LinkedList class to implement a queue
class Queue:
    def __init__(self):
        self.linkedList = LinkedList()  # Create a linked list object for the queue

    def enqueue(self, value):
        # Enqueue (insert) a new node with the given value into the queue
        self.linkedList.enqueue(value)

    def dequeue(self):
        # Dequeue (remove and return) a node from the front of the queue
        return self.linkedList.dequeue()

    def isempty(self):
        # Check if the queue is empty by examining the head of the linked list
        return self.linkedList.isempty()


# Define a TreeNode class for the binary tree
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Create a binary tree
newBT = TreeNode("Drinks")
leftChild = TreeNode("hot")
rightChild = TreeNode("cold")
newBT.left = leftChild
newBT.right = rightChild


def deleteBT(rootNode):
    rootNode.data = None
    rootNode.left = None
    rootNode.right = None
    return "the BT has been sucessfully deleted"
