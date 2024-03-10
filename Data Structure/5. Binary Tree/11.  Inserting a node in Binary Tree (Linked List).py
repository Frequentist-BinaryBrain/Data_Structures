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

def searchBT(rootNode, nodeValue):
    if not rootNode:
        return "Binary tree does not exist"
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)

        while not customQueue.isempty():
            root = customQueue.dequeue()

            if root.value.data == nodeValue:
                return "Success: Node found in the binary tree"

            if root.value.left is not None:
                customQueue.enqueue(root.value.left)

            if root.value.right is not None:
                customQueue.enqueue(root.value.right)

        return "Not found: Node not present in the binary tree"

def insert_node(rootNode, newNodeValue):
    # Check if the binary tree is empty
    if not rootNode:
        # If empty, create a new tree node with the given value
        rootNode = TreeNode(newNodeValue)
        # Return the data of the newly inserted node
        return rootNode.data

    # Create a queue for level-order traversal
    customQueue = Queue()
    customQueue.enqueue(rootNode)

    # Perform level-order traversal to find a suitable position for insertion
    while not customQueue.isempty():
        root = customQueue.dequeue()

        # Check if the left child of the current node is empty
        if root.value.left is not None:
            # If not empty, enqueue the left child for further traversal
            customQueue.enqueue(root.value.left)
        else:
            # If empty, insert a new node with the given value as the left child
            root.value.left = TreeNode(newNodeValue)
            # Return the data of the newly inserted node
            return root.value.left.data

        # Check if the right child of the current node is empty
        if root.value.right is not None:
            # If not empty, enqueue the right child for further traversal
            customQueue.enqueue(root.value.right)
        else:
            # If empty, insert a new node with the given value as the right child
            root.value.right = TreeNode(newNodeValue)
            # Return the data of the newly inserted node
            return root.value.right.data

# Example usage:
# Insert "Coca Cola" into the binary tree and print the level-order traversal
insert_node(newBT, "Coca Cola")
levelOrderTraversal(newBT)




