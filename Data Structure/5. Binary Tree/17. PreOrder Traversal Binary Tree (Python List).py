class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    def insertNode(self, value):
        # Check if the binary tree is already full
        if self.lastUsedIndex + 1 == self.maxSize:
            return "Binary Tree is full"

        # Insert the new value into the customList at the next available index
        self.customList[self.lastUsedIndex + 1] = value

        # Update lastUsedIndex to reflect the newly inserted node
        self.lastUsedIndex += 1

    def searchNode(self, nodeValue):
        for i in range(len(self.customList)):
            if self.customList[i] == nodeValue:
                return "Success"
        return "Not Found"

    def preOrderTraversal(self, index):
        # This method performs pre-order traversal of the binary tree, starting from the given index.

        # Check if the given index is beyond the last used index, indicating an empty or invalid node.
        if index > self.lastUsedIndex:
            return

        # Print the value of the current node in the traversal.
        print(self.customList[index])

        # Recursively perform pre-order traversal on the left child (index*2) of the current node.
        self.preOrderTraversal(index * 2)

        # Recursively perform pre-order traversal on the right child (index*2 + 1) of the current node.
        self.preOrderTraversal(index * 2 + 1)


