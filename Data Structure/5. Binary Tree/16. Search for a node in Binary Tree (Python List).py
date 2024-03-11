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

newBT = BinaryTree(7)
newBT.insertNode("Drinks")
newBT.insertNode("Hot")
newBT.insertNode("Cold")
print(newBT.searchNode("Hot"))
