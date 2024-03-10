#   Definition: Preorder traversal involves visiting the root node first, then traversing the left subtree, and finally traversing the right subtree.
#
# Logical Flow:
#
#     Visit the root node.
#     Traverse the left subtree (recursively).
#     Traverse the right subtree (recursively).

#         N1
#        /  \
#       N2   N3
#      /  \    \
#     N4   N9   N6
#         / \   / \
#        N10 N5 N7 N8

#   The preorder traversal sequence: N1, N2, N4, N9, N10, N5, N3, N6, N7, N8

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


# # Adding more child nodes to the existing tree
# newBT.left.left = TreeNode("Tea")
# newBT.left.right = TreeNode("Coffee")
#
# newBT.right.left = TreeNode("Cola")
# newBT.right.right = TreeNode("Fanta")

# Define a function for preorder tree traversal
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

# Call the preorder traversal function starting from the root of the tree
preOrderTraversal(newBT)
