#   The levelOrder traversal is a tree traversal method where you visit the nodes level by level, starting from the root node and moving down
#   to the leaves.
#   This traversal is achieved using a queue data structure.

#             N1
#            /  \
#          N2   N3
#         / \   / \
#        N4 N5 N6 N7
#              |
#             N8

#       First Level:
#         Visit the root node: N1
#
#     Second Level:
#         Visit the left child of the root: N2
#         Visit the right child of the root: N3
#
#     Third Level:
#         Visit the left children of the second level: N4, N5
#         Visit the right children of the second level: N6, N7
#
#     Fourth Level:
#         Visit the left child of the third level (N4): N8
#         Visit the right child of the third level (N5): (No right child)
#
# So, the levelOrder traversal sequence for the given example is: N1, N2, N3, N4, N5, N6, N7, N8.
#
# The implementation involves using a queue to keep track of the nodes at each level.
# The process includes enqueuing the root node, and in each iteration, dequeue a node, print its value, and enqueue its children (if they exist).

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


# Function to perform level-order traversal using the provided Queue
#   https://youtu.be/86g8jAQug04?si=VO9ohNxbaWYVcI7_ watch this to understand

def levelOrderTraversal(rootNode):
    # Check if the tree is empty (no root node)
    if not rootNode:
        return

    # Create a customQueue using the Queue class to perform level-order traversal
    customQueue = Queue()

    # Enqueue the root node to start the traversal
    customQueue.enqueue(rootNode)  # This brings the first node in the queue

    # Continue traversal until the queue is empty
    while not customQueue.isempty():
        current_node = customQueue.dequeue()

        # Print the data of the current node being visited
        print(current_node.value.data)

        # Enqueue the left child of the current node if it exists
        if current_node.value.left is not None:
            customQueue.enqueue(current_node.value.left)

        # Enqueue the right child of the current node if it exists
        if current_node.value.right is not None:
            customQueue.enqueue(current_node.value.right)


# Create a binary tree
newBT = TreeNode("Drinks")
leftChild = TreeNode("hot")
rightChild = TreeNode("cold")
newBT.left = leftChild
newBT.right = rightChild

# Perform level-order traversal
print("LevelOrder Traversal:")
levelOrderTraversal(newBT)
