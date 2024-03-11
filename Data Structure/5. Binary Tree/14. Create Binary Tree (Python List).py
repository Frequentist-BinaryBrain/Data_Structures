# Index calculations are done as follows:
#     Left child index = 2 * parent index
#     Right child index = 2 * parent index + 1

#
#     10
#    /  \
#   20   30
#  / \   /
# 40 50 60

#   Index:  1  2  3  4  5  6
#  Array: [10,20,30,40,50,60]

#   In this example:
#
#     The root node (10) is at index 1.
#     The left child of 10 is calculated as 2 * 1 = 2, and the right child is 2 * 1 + 1 = 3.
#     The left child of 20 is 2 * 2 = 4, and the right child is 2 * 2 + 1 = 5.
#     The left child of 30 is 2 * 3 = 6.


#       Binary Tree Class Initialization:
#         Create an object of the binary tree class.
#         Initialize a fixed-size Python list.
#         Set the lastUsedIndex variable to zero.
#
#     Purpose of lastUsedIndex:
#         The lastUsedIndex variable is used to track the last cell that was used in the Python list.
#         It helps in managing the insertion of new nodes by providing information about where the next node should be placed.
#         During the insertion of a new node:
#             The algorithm uses the lastUsedIndex to determine the position for inserting the new node.
#             Knowing the last used index simplifies the process of finding the appropriate location for the new node, making the insertion method more efficient.


#NOTE: for simplicity we wont use index zero and starts from index:1

class BinaryTree:

    def __init__(self, size):
        # Create a customList with a fixed size, initialized to None
        self.customList = size * [None]

        # Initialize the lastUsedIndex to 0
        self.lastUsedIndex = 0

        # Set the maximum size for the binary tree
        self.maxSize = size

#   customList:
#     It initializes a list (customList) with a fixed size, where each element is initially set to None. This list will represent the binary tree structure.
#
# lastUsedIndex:
#     This variable keeps track of the last used index in the customList.
#     It starts at 0, indicating that no elements have been inserted yet.
#
# maxSize:
#     This attribute specifies the maximum size of the binary tree.
#     It helps in managing the size limitation of the binary tree based on the provided size parameter.

newBT = BinaryTree(8)

