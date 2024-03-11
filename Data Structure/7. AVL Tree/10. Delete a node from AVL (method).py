class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


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


def getHeight(rootNode):
    if not rootNode:
        return 0
    return rootNode.height


def rightRotate(disbalanceNode):
    newRoot = disbalanceNode.left
    disbalanceNode.left = disbalanceNode.left.right
    newRoot.right = disbalanceNode
    disbalanceNode.height = 1 + max(getHeight(disbalanceNode.left), getHeight(disbalanceNode.right))
    newRoot.height = 1 + max(getHeight(newRoot.left), getHeight(newRoot.right))
    return newRoot


def leftRotate(disbalanceNode):
    newRoot = disbalanceNode.right
    disbalanceNode.right = disbalanceNode.right.left
    newRoot.left = disbalanceNode
    disbalanceNode.height = 1 + max(getHeight(disbalanceNode.left), getHeight(disbalanceNode.right))
    newRoot.height = 1 + max(getHeight(newRoot.left), getHeight(newRoot.right))
    return newRoot


def getBalance(rootNode):
    if not rootNode:
        return 0
    return getHeight(rootNode.left) - getHeight(rootNode.right)


def insertNode(rootNode, nodeValue):
    if not rootNode:
        return AVLNode(nodeValue)
    elif nodeValue < rootNode.data:
        rootNode.left = insertNode(rootNode.left, nodeValue)
    else:
        rootNode.right = insertNode(rootNode.right, nodeValue)

    rootNode.height = 1 + max(getHeight(rootNode.left), getHeight(rootNode.right))
    balance = getBalance(rootNode)

    if balance > 1 and nodeValue < rootNode.left.data:
        return rightRotate(rootNode)

    if balance > 1 and nodeValue > rootNode.left.data:
        rootNode.left = leftRotate(rootNode.left)
        return rightRotate(rootNode)

    if balance < -1 and nodeValue > rootNode.right.data:
        return leftRotate(rootNode)

    if balance < -1 and nodeValue < rootNode.right.data:
        rootNode.right = rightRotate(rootNode.right)
        leftRotate(rootNode)

    return rootNode


#   Before proceeding with the deletion method, it is essential to establish a helper function. This function will be designed to retrieve the minimum
#   value within the AVL tree. Its purpose becomes crucial during the removal of a node from an AVL tree containing two children. In such scenarios,
#   the function aids in identifying the successor of the node to be deleted. This successor, obtained by selecting the minimum value from the right subtree,
#   is a key component for our deletion process. Hence, the implementation of this method is imperative.
# " 7. Insert a node in AVL (Python)" You will find regarding successor over here


def getMinValue(
        rootNode):  # used to find min value. This function is used in delete node to find min value in right subtree
    if rootNode is None or rootNode.left is None:
        return rootNode
    return getMinValue(rootNode.left)


def deleteNode(rootNode, nodeValue):
    if not rootNode:
        return rootNode  # If the tree is empty or the node is not found, return the original root

    elif nodeValue < rootNode.data:
        rootNode.left = deleteNode(rootNode.left, nodeValue)  # Recursively delete the node in the left subtree
    elif nodeValue > rootNode.data:
        rootNode.right = deleteNode(rootNode.right, nodeValue)  # Recursively delete the node in the right subtree
    else:  # This block executes when the node to be deleted is found
        if rootNode.left is None:
            temp = rootNode.right
            rootNode = None
            return temp  # If the node has no left child, replace it with its right child
        elif rootNode.right is None:
            temp = rootNode.left
            rootNode = None
            return temp  # If the node has no right child, replace it with its left child

        temp = getMinValue(rootNode.right)  # Get the successor node from the right subtree
        rootNode.data = temp.data  # Copy the data of the successor to the current node
        rootNode.right = deleteNode(rootNode.right, temp.data)  # Delete the successor node

    # Update the height of the current node
    rootNode.height = 1 + max(getHeight(rootNode.left), getHeight(rootNode.right))
    balance = getBalance(rootNode)  # Get the balance factor of the current node

    # Check Left Left condition
    if balance > 1 and getBalance(rootNode.left) >= 0:
        return rightRotate(rootNode)  # Perform right rotation for Left Left condition
    # Check Right Right condition
    if balance < -1 and getBalance(rootNode.right) <= 0:
        return leftRotate(rootNode)  # Perform left rotation for Right Right condition
    # Check Left Right condition
    if balance > 1 and getBalance(rootNode.left) < 0:
        rootNode.left = leftRotate(rootNode.left)  # Left rotate the left child first
        return rightRotate(rootNode)  # Right rotate for Left Right condition
    # Check Right Left condition
    if balance < -1 and getBalance(rootNode.right) > 0:
        rootNode.right = rightRotate(rootNode.right)  # Right rotate the right child first
        return leftRotate(rootNode)  # Left rotate for Right Left condition

    return rootNode  # Return the root of the (potentially rotated) subtree


def deleteAVL(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The AVL has been successfully deleted"

newAVL = AVLNode(5)
newAVL = insertNode(newAVL, 10)
newAVL = insertNode(newAVL, 15)
newAVL = insertNode(newAVL, 20)
newAVL = deleteNode(newAVL, 15)
levelOrdertraversal(newAVL)
