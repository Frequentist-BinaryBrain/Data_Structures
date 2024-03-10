#   # Binary Search Tree (BST) - Traversal Methods:
#
# # In a binary search tree, there are four main methods to traverse through nodes:
# # 1. PreOrder Traversal
# # 2. InOrder Traversal
# # 3. PostOrder Traversal
# # 4. LevelOrder Traversal

class BSTNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insertNode(rootNode, nodeValue):
    if rootNode.data is None:
        rootNode.data = nodeValue
    elif nodeValue < rootNode.data:
        if rootNode.left is None:
            rootNode.left = BSTNode(nodeValue)
        else:
            insertNode(rootNode.left, nodeValue)
    else:
        if rootNode.right is None:
            rootNode.right = BSTNode(nodeValue)
        else:
            insertNode(rootNode.right, nodeValue)
    return "Node has been successfully inserted"


#   # - PreOrder Traversal:
# #   - Visit the root node first, then the left subtree, and finally the right subtree.
# #   - Recursive approach is used to traverse the tree.
# #   - Time and space complexity: O(n), where n is the number of nodes.

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.left)
    preOrderTraversal(rootNode.right)


#   # - InOrder Traversal:
# #   - Visit the left subtree first, then the root node, and finally the right subtree.
# #   - Recursive approach is used to traverse the tree.
# #   - Time and space complexity: O(n), where n is the number of nodes.

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.left)
    print(rootNode.data)
    inOrderTraversal(rootNode.right)


#   # - PostOrder Traversal:
# #   - Visit the left subtree first, then the right subtree, and finally the root node.
# #   - Recursive approach is used to traverse the tree.
# #   - Time and space complexity: O(n), where n is the number of nodes


def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.left)
    postOrderTraversal(rootNode.right)
    print(rootNode.data)


#   # - LevelOrder Traversal:
# #   - Visit nodes level by level, starting from the left child and continuing to the right child.
# #   - Queue data structure is used to traverse through all nodes.
# #   - Time and space complexity: O(n), where n is the number of nodes.

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
