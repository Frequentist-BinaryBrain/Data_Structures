#   Left Left Condition:
#
# Scenario:
#
#     The Left Left condition in AVL trees occurs when a new node is inserted into the left subtree of the left child of a node, causing an imbalance in the tree.
#
# Imbalance Detection:
#
#     Compare the heights of the left and right subtrees of a node.
#     If the left subtree's height is more than one greater than the right subtree's height, the Left Left condition is identified.

#         50
#        / \
#       30  70
#      / \
#     20  40

#   Inserting Node 10:
# Let's say we want to insert a node with the value 10 into this AVL tree. The steps involve comparing the value with each node's value and navigating through the tree.
#
#     Compare 10 with the root (50), find that 10 is less, and go to the left subtree.
#     Compare 10 with the left child (30), find that 10 is less, and go to the left subtree.
#     Compare 10 with the left child (20), find that 10 is less, and insert it as the left child of 20.
#
# After inserting node 10, the tree becomes:
#         50
#        / \
#       30  70
#      / \
#     20  40
#    /
#   10

#   Imbalance Detection After Insertion:
#
#     Start from the inserted node (10) and move up to the root.
#
#     Check the height difference between the left and right subtrees at each node.
#         For node 10: The left subtree's height is 0, and the right subtree's height is 0 (balanced).
#         For node 20: The left subtree's height is 1, and the right subtree's height is 0 (balanced).
#         For node 30: The left subtree's height is 2, and the right subtree's height is 1 (balanced).
#         For node 50: The left subtree's height is 3, and the right subtree's height is 1 (imbalanced).

# Left Left Condition Identified:
# Since the left subtree of node 30 is more than one greater than the right subtree, we have a Left Left condition.
#
# Algorithm for Handling Left Left:
#
#     Perform a right rotation on the imbalanced node (30 in this case).
#     Update the heights of the imbalanced node and the new root.

#        30
#       / \
#      20  50
#     /   / \
#    10  40  70
#   Now, the tree is balanced, and the Left Left condition has been successfully addressed.

def right_rotation(disbalance_node):
    new_root = disbalance_node.left  # Create a new root based on the left child of the imbalanced node
    disbalance_node.left = new_root.right  # Set imbalanced node's left child to its left child's right child
    new_root.right = disbalance_node  # Set the new root's right child to the imbalanced node
    # update height of disbalancednode and new root
    # return newroot

#       Find the Disbalanced Node:
#         Identify the node in the AVL tree causing the imbalance.
#
#     Identify the Grandchild:
#         Look for the grandchild(Select the grandchild whose height is more is we have two spilts) of the disbalanced node that contributes to the imbalance. This grandchild will determine the condition.
#         Traverse from the disbalanced node towards the grandchild, noting the direction of each step.
#
#     Determine the Condition:
#         The path from the disbalanced node to the grandchild indicates the condition.
#         For example, if the path involves going left, then left again (LL), it's a Left Left condition.
#
#     Select Rotation:
#         Based on the identified condition, apply the appropriate rotation to rebalance the tree.
#         For Left Left condition (LL), perform a right rotation.
