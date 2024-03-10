#   Consider a binary tree like this:
#             N1
#            /  \
#          N2   N3
#         / \   / \
#        N4 N5 N6 N7
#               |
#               N8

#   In InOrder traversal, we visit the left subtree first,
#                                       the root node
#                             then the right subtree.
#                                   .
#
#     For our example:
#
#     Start with the left subtree of N1:
#         Visit N4, N2, N5 , N1
#     Move to the right subtree of N1:
#         Visit N8, N6, N3, N7,
#
#
# So, the InOrder traversal sequence is N4, N2, N5 , N1, N8, N6, N3, N7

# Define the TreeNode class for a binary tree node
# Define the TreeNode class for a binary tree node
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Create a binary tree with the root node "Drinks"
newBT = TreeNode("Drinks")

# Create left and right children nodes for "Drinks"
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")

# Connect the left and right children nodes to the root node
newBT.left = leftChild
newBT.right = rightChild

def preOrderTraversal(rootNode):
    # Base case: If the current node is None, return
    if not rootNode:  # --------> O(1)
        return

    # Print the data of the current node (root)
    print(rootNode.data)  # --------> O(1)

    # Recursively traverse the left subtree
    preOrderTraversal(rootNode.left)  # --------> O(n/2)

    # Recursively traverse the right subtree
    preOrderTraversal(rootNode.right) # --------> O(n/2)

def InOrderTraversal(rootNode):
    # Base case: If the root node is None, return
    if not rootNode:
        return

    # Recursively traverse the left subtree
    InOrderTraversal(rootNode.left)

    # Print the data of the root node
    print(rootNode.data)

    # Recursively traverse the right subtree
    InOrderTraversal(rootNode.right)

# Perform InOrder traversal starting from the root node of the binary tree
InOrderTraversal(newBT)

