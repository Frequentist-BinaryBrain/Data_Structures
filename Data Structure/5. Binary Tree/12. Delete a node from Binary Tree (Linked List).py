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


#   Delete Node in Binary Tree (Linked List) - Explanation and Implementation
#
# In the context of deleting a node from a binary tree implemented as a linked list, we can follow a two-step process.
# First, we'll find and delete the deepest node, and then
# we'll replace the target node's value with that of the deepest node.


# First

#   Get Deepest Node Function:
#
#     The function traverses the binary tree using level-order traversal.
#     It initializes a custom queue and enqueues the root node to start the traversal.
#     While the queue is not empty, it dequeues the front node and enqueues its left and right children if they exist.
#     The last node visited becomes the deepest node.
#     Returns the data of the deepest node.

def deepest_node(rootNode):
    # Check if the binary tree is empty
    if not rootNode:
        return

    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)

        while not customQueue.isempty():
            root = customQueue.dequeue()

            # Enqueue the left child if it exists
            if root.value.left is not None:
                customQueue.enqueue(root.value.left)

            # Enqueue the right child if it exists
            if root.value.right is not None:
                customQueue.enqueue(root.value.right)

        # After the while loop, 'root' will be the last node processed, which is the deepest node
        deepestNode = root.value
        return deepestNode


print("Deepest Node is: ", deepest_node(newBT).data)  # Because tree call has data parameter


# Second Step
#   Delete Deepest Node Function:
#
#     It takes the root node and the deepest node as parameters.
#     Similar to the get_deepest_node function, it traverses the tree and deletes the deepest node.
#     If the right child is the deepest node, it sets the right child to None; otherwise, it enqueues it for further traversal.
#     If the left child is the deepest node, it sets the left child to None; otherwise, it enqueues it.
#     Deletes the deepest node from the binary tree.

def deleteDeepestNode(rootNode, dNode):  # dNode is the deepest node we found from above
    if not rootNode:
        return
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)

        while not customQueue.isempty():
            root = customQueue.dequeue()
            if root.value is dNode:
                root.value = None
                return
            if root.value.right:
                if root.value.right is dNode:
                    root.value.right = None
                    return
                else:
                    customQueue.enqueue(root.value.right)

            if root.value.left:
                if root.value.left is dNode:
                    root.value.left = None
                    return
                else:
                    customQueue.enqueue(root.value.left)

newNode = deepest_node(newBT)
deleteDeepestNode(newBT, newNode)
levelOrderTraversal(newBT) # You can see cold node is deleted because it is the deepest node
print("-----------------------------------------------")


#   Third Step

#   Delete Node Function:
#
#     The main function to delete a node from the binary tree.
#     It uses level-order traversal to find and delete the target node.
#     If the target node is found, it replaces its value with that of the deepest node.
#     Then, it calls delete_deepest_node to delete the deepest node from the tree.

def delete_node(rootNode, node):

    if not rootNode:
        return
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)

        while not customQueue.isempty():
            root = customQueue.dequeue()
            if root.value.data == node:
                root.value.data = deepest_node(rootNode).data
                deleteDeepestNode(rootNode, deepest_node(rootNode))
                return "Node is successfully deleted"
            if root.value.left:
                customQueue.enqueue(root.value.left)
            if root.value.right:
                customQueue.enqueue(root.value.right)
        return "Node not present in the tree"

newBT = TreeNode("Drinks")
leftChild = TreeNode("hot")
rightChild = TreeNode("cold")
newBT.left = leftChild
newBT.right = rightChild

delete_node(newBT, "hot")
levelOrderTraversal(newBT)
