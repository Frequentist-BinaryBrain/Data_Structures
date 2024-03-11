#   Left Right Condition:
#
# Scenario:
#
#     The Left Right condition arises when a new node is inserted into the right subtree of the left child of a node, causing an imbalance in the tree.
#
# Imbalance Detection:
#
#     Compare the heights of the left and right subtrees of a node.
#     If the left subtree's height is more than one greater than the right subtree's height, further analyze the left child's right subtree.
#     If the left child's right subtree's height is greater than its left subtree's height, the Left Right condition is identified.
#
# Example AVL Tree:
# Consider the following AVL tree:
#          70
#        /   \
#       50    90
#      / \    / \
#     30  60 80 100
#    /
#   20

#   Inserting Node 25:
# Compare with Root (70): 25 is less than 70, move to the left subtree.
# Compare with Left Child (50): 25 is less than 50, move to the left subtree.
# Compare with Left Child (30): 25 is greater than 20 but less than 30, insert as the right child of 20.

#          70
#        /   \
#       50    90
#      / \    / \
#     30  60 80 100
#    /
#   20
#    \
#     25

# Node 30 has imbalance (grandchild will be taken with the highest length, in this case we take 25 though it is right node because it is grandchild)
# Path to the grand child from disbalanced node is left and then right  so it is left right condition

# For left right condition we do left rotation first and then right rotation next

# Left Rotation - left rotation to the child of disbalanced node.

#          70
#        /   \
#       50    90
#      / \    / \
#     30  60 80 100
#    /
#   25
#   /
#  20

# Right rotation - for disbalanced node

# #          70
# #        /   \
# #       50    90
# #      / \    / \
# #     25  60 80 100
# #    / \
# #   20  30


#    Algorithm of LEFT RIGHT Condition

# Step - 1: Rotate disbalancedNode.Leftchild
# Step - 2: Rotate Right disbalanced Node

# Step - 1

# Step - 1: Rotate disbalancedNode.Leftchild
def rotateLeft(disbalancedNode):
    # Store the right child of disbalancedNode
    newRoot = disbalancedNode.rightChild

    # Update the right child of disbalancedNode to be the left child of newRoot
    disbalancedNode.rightChild = newRoot.leftChild

    # Set the left child of newRoot to be the original disbalancedNode
    newRoot.leftChild = disbalancedNode
    # update height of disbalancedNode and newRoot
    return newRoot


# Step - 2
# Step - 2: Rotate Right disbalanced Node
def rotateRight(disbalancedNode):
    # Store the left child of disbalancedNode
    newRoot = disbalancedNode.leftChild

    # Update the left child of disbalancedNode to be the right child of newRoot
    disbalancedNode.leftChild = newRoot.rightChild

    # Set the right child of newRoot to be the original disbalancedNode
    newRoot.rightChild = disbalancedNode

    # update height of disbalancedNode and newRoot
    return newRoot
