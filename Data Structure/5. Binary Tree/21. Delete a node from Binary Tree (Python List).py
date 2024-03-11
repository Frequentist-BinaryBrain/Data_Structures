class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    def insertNode(self, value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "Binary Tree is full"
        self.customList[self.lastUsedIndex + 1] = value
        self.lastUsedIndex += 1

    def searchNode(self, nodeValue):
        for i in range(len(self.customList)):
            if self.customList[i] == nodeValue:
                return "Success"
        return "Not Found"

    def preOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        print(self.customList[index])
        self.preOrderTraversal(index * 2)
        self.preOrderTraversal(index * 2 + 1)

    def inOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.inOrderTraversal(index * 2)
        print(self.customList[index])
        self.inOrderTraversal(index * 2 + 1)

    def postOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.postOrderTraversal(index * 2)
        self.postOrderTraversal(index * 2 + 1)
        print(self.customList[index])

    def levelOrderTraversal(self, index):
        for i in range(index, self.lastUsedIndex + 1):
            print(self.customList[i])


#     Finding the Deepest Node:
#     The deepest node is the last node reached during a level-order traversal.
#     In Python list, it corresponds to the node at the end of the last used index.
#
# 2. Replacement Strategy:
#     To avoid breaking the tree structure, the node to be deleted is replaced by the value of the deepest node.
#     The value of the deepest node is then set to None, and the last used index is decremented.


#        N1
#       /  \
#     N2    N3
#     / \   / \
#    N4 N5 N6 N7
#   / \
#  N8  N9

# If you want to delete N3, we cant directly delete becauase if we do then N6 and N7 will also be deleted by garbage collector like below
#        N1
#       /
#     N2
#     / \
#    N4 N5
#   / \
#  N8  N9

# So to avoid this we find the deepest node and replace the node we want to delete with the deepest node like below

#        N1
#       /  \
#     N2    N9
#     / \   / \
#    N4 N5 N6 N7
#   /
#  N8


    def deleteNode(self, value):
        # Check if there are elements in the tree
        if self.lastUsedIndex == 0:
            return "No element to delete"

        # Loop through the tree to find the node to delete
        for i in range(1, self.lastUsedIndex + 1):
            # Check if the current node contains the value to delete
            if self.customList[i] == value:
                # Replace the node with the deepest node and update the tree
                self.customList[i] = self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1  # Decrement the lastUsedIndex as a node has been deleted
                return "The node has been deleted"

        # If the value to delete is not found in any node
        return "Node not found"

    def deleteBT(self):
        self.customList = None
        return "Binary Tree has been deleted"

newBT = BinaryTree(8)
newBT.insertNode("Drinks")
newBT.insertNode("Hot")
newBT.insertNode("Cold")
newBT.insertNode("Tea")
newBT.insertNode("COla")
print(newBT.customList)
print(newBT.deleteNode("Hot"))
print(newBT.customList)
