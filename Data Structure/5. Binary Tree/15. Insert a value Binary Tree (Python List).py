#   Two Insertion Scenarios:
#
#     Scenario 1: Binary Tree is Full
#         If the binary tree is already full, a message is returned indicating that the tree is full.
#         Unlike linked lists, a fixed size is chosen for the Python list to manage time complexity, even though Python lists can be dynamically sized.
#
#     Scenario 2: Vacant Place in Python List
#         When a vacant place is available in the Python list, a new node can be inserted.
#         A level-order traversal is used to find a vacant place in the binary tree.
#         Insertion involves calculating the index based on the parent node's index.
#         In the example below, a new node is inserted as the left child of N5(identified using level order traversal) , and the
#         Python list is updated accordingly.


#        N1
#       /  \
#     N2    N3
#     / \   / \
#    N4 N5 N6 N7
#   / \
#  N8  N9


#         N1
#       /   \
#     N2     N3
#    /  \    / \
#   N4   N5 N6  N7
#  / \   /
# N8 N9 (new)

#   Now we know that the left child of N5 should be located in the Python list based on the equation
#   Left child index = 2 * parent index
#   Right child index = 2 * parent index + 1
#   #   Index:1  2   3   4   5   6   7   8   9
# #  Array: [N1, N2, N3, N4, N5, N6, N7, N8, N9, new]

#   So here index of N5 is 5 and to calculate index of left child of N5 is
#   #   Left child index = 2 * parent index = 2 * 5 = 10

#   #   Index:1  2   3   4   5   6   7   8   9   10
# #  Array: [N1, N2, N3, N4, N5, N6, N7, N8, N9, new]

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


newBT = BinaryTree(7)
newBT.insertNode("Drinks")
newBT.insertNode("Hot")
newBT.insertNode("Cold")
print(newBT.customList)  # First index 0 will always be None because we start from Index 1
