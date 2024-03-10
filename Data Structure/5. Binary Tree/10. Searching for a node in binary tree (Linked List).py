#   Why Level-Order Traversal for Searching:
#
#     Level-order traversal is a general-purpose method that explores the binary tree in a breadth-first manner.
#     It is well-suited for scenarios where the goal is to find a node without specific ordering requirements.
#     Level-order traversal ensures that nodes at the same level are visited before moving on to the next level, which may be beneficial in certain applications.


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

    def enqueue(self, value):
        newNode = Node(value)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def isempty(self):
        return self.head is None

    def dequeue(self):
        if self.isempty():
            return None
        else:
            current_node = self.head

            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next

            return current_node


class Queue:
    def __init__(self):
        self.linkedList = LinkedList()

    def enqueue(self, value):
        self.linkedList.enqueue(value)

    def dequeue(self):
        return self.linkedList.dequeue()

    def isempty(self):
        return self.linkedList.isempty()


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

newBT = TreeNode("Drinks")
leftChild = TreeNode("hot")
rightChild = TreeNode("cold")
newBT.left = leftChild
newBT.right = rightChild

def levelOrderTraversal(rootNode):
    if not rootNode:
        return

    customQueue = Queue()
    customQueue.enqueue(rootNode)

    while not customQueue.isempty():
        root = customQueue.dequeue()
        print(root.value.data)

        if root.value.left is not None:
            customQueue.enqueue(root.value.left)

        if root.value.right is not None:
            customQueue.enqueue(root.value.right)



# Definition of the searchBT function
def searchBT(rootNode, nodeValue):
    # Check if the binary tree exists
    if not rootNode:
        return "Binary tree does not exist"
    else:
        # Create a custom queue for level-order traversal
        customQueue = Queue()
        customQueue.enqueue(rootNode)  # To insert node to a queue

        # Perform level-order traversal
        while not customQueue.isempty():    #  While customqueue is not empty
            # Dequeue the front node in the queue
            root = customQueue.dequeue()   # This brings the first node in the queue

            # Check if the current node has the desired value
            if root.value.data == nodeValue:
                return "Success: Node found in the binary tree"

            # Enqueue the left child if it exists
            if root.value.left is not None:
                customQueue.enqueue(root.value.left)

            # Enqueue the right child if it exists
            if root.value.right is not None:
                customQueue.enqueue(root.value.right)

        # If the value is not found after traversal, return a message indicating it
        return "Not found: Node not present in the binary tree"


result = searchBT(newBT, "hot")
print(result)



