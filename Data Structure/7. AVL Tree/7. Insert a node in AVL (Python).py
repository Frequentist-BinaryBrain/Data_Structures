class AVLNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1  # Initialize the height of a new node to 1


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


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


def levelOrdertraversal(rootNode):
    if not rootNode:
        return

    customQueue = Queue()
    customQueue.enqueue(rootNode)

    while not customQueue.isempty():
        root = customQueue.dequeue()
        print(root.value.data, end=" ")
        if root.value.left is not None:
            customQueue.enqueue(root.value.left)
        if root.value.right is not None:
            customQueue.enqueue(root.value.right)


# This is from BST
def searchNode(rootNode, nodeValue):
    if rootNode.data == nodeValue:
        print("The value is found")
    elif nodeValue < rootNode.data:
        if rootNode.leftChild.data == nodeValue:
            print("The value is found")
        else:
            searchNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild.data == nodeValue:
            print("The value is found")
        else:
            searchNode(rootNode.rightChild, nodeValue)


def getHeight(rootNode):
    if not rootNode:
        return 0  # Return 0 if the node is None (base case)
    return rootNode.height  # Return the height of the node


def rightRotate(disbalanceNode):
    newRoot = disbalanceNode.left  # Store the left child of the disbalanced node
    disbalanceNode.left = disbalanceNode.left.right  # We are just removing disbalanced node left child connection as new Node bcx its now new node right child
    newRoot.right = disbalanceNode  # Make disbalanced node the right child of the new root

    # Update heights of the rotated nodes
    disbalanceNode.height = 1 + max(getHeight(disbalanceNode.left), getHeight(disbalanceNode.right))
    newRoot.height = 1 + max(getHeight(newRoot.left), getHeight(newRoot.right))

    return newRoot  # Return the new root of the rotated subtree


def leftRotate(disbalanceNode):
    newRoot = disbalanceNode.right  # Store the right child of the disbalanced node
    disbalanceNode.right = disbalanceNode.right.left  # Make the right child's left subtree the new right subtree of disbalanced node
    newRoot.left = disbalanceNode  # Make disbalanced node the left child of the new root

    # Update heights of the rotated nodes
    disbalanceNode.height = 1 + max(getHeight(disbalanceNode.left), getHeight(disbalanceNode.right))
    newRoot.height = 1 + max(getHeight(newRoot.left), getHeight(newRoot.right))

    return newRoot  # Return the new root of the rotated subtree


def getBalance(rootNode):
    if not rootNode:
        return 0  # Return 0 if the node is None (base case)
    return getHeight(rootNode.left) - getHeight(rootNode.right)  # Calculate the balance factor


def insertNode(rootNode, nodeValue):
    if not rootNode:
        return AVLNode(nodeValue)  # Create a new node with the given value if the current node is None
    elif nodeValue < rootNode.data:
        rootNode.left = insertNode(rootNode.left, nodeValue)  # Insert into the left subtree if the value is smaller
    else:
        rootNode.right = insertNode(rootNode.right, nodeValue)  # Insert into the right subtree if the value is larger

    # Update height of the current node
    rootNode.height = 1 + max(getHeight(rootNode.left), getHeight(rootNode.right))
    balance = getBalance(rootNode)  # Get the balance factor of the current node

    # Check Left Left condition
    if balance > 1 and nodeValue < rootNode.left.data:
        return rightRotate(rootNode)

    # Check Left Right condition
    if balance > 1 and nodeValue > rootNode.left.data:
        rootNode.left = leftRotate(rootNode.left)  # First child node left rotate
        return rightRotate(rootNode)  # imbalanced node right rotate

    # Check Right Right condition
    if balance < -1 and nodeValue > rootNode.right.data:
        return leftRotate(rootNode)

    # Check Right Left condition
    if balance < -1 and nodeValue < rootNode.right.data:
        rootNode.right = rightRotate(rootNode.right)  # right rotate child node first
        return leftRotate(rootNode)  # Left rotate imbalanced node

    return rootNode  # Return the root of the (potentially rotated) subtree


newAVL = AVLNode(5)
newAVL = insertNode(newAVL, 10)
newAVL = insertNode(newAVL, 15)
newAVL = insertNode(newAVL, 20)
levelOrdertraversal(newAVL)
