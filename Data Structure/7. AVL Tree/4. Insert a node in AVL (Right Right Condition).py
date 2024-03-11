#   Right Right Condition:
#
# Scenario:
#
#     The Left Right condition arises when a new node is inserted into the right subtree of the right child of a node, causing an imbalance in the tree
#
# Imbalance Detection:
#
#     Compare the heights of the left and right subtrees of a node.
#     If the right subtree's height is more than one greater than the left subtree's height, further analyze the right child's left subtree.
#     If the right child's left subtree's height is greater than its right subtree's height, the right Right condition is identified.
#
# Example AVL Tree:
# Consider the following AVL tree:
#          50
#        /   \
#       40    60
#              \
#               65
#

#   Inserting Node 70:
#          50
#        /   \
#       40    60
#              \
#               65
#                \
#                 70


# Node 60 has imbalance - We do LEFT rotation of imbalanced Node for RIGHT RIGHT condition

#          50
#        /    \
#       40     65
#             / \
#           60   70


#    Algorithm of RIGHT RIGHT Condition

# Step - 1: Rotate LEFT - disbalancedNode

def left_rotation(disbalance_node):
    # Store the new root, which is the right child of the disbalanced node
    new_root = disbalance_node.right

    # Update the right child of disbalanced node to be the left child of the new root
    disbalance_node.right = disbalance_node.right.left

    # Make the disbalanced node the left child of the new root
    new_root.left = disbalance_node

    # update height of disbalancednode and new root
    # return newroot
