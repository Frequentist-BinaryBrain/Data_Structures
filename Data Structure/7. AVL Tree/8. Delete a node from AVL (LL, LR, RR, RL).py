#   Case 1: Rotation is Not Required


# Subcase 1: Node to be Deleted is a Leaf Node (Example: Deleting 40)
#
#     Begin the search for the node starting from the root.
#     Traverse left or right based on the comparison with the current node's value.
#     When the node to be deleted is found, simply remove it since it's a leaf node.

#   Before Deletion:
#          70
#        /    \
#       50     90
#      /  \    / \
#     30   60 80 100
#    / \
#   20  40

# After Deletion (Leaf Node 40):
#          70
#        /    \
#       50     90
#      /  \    / \
#     30   60 80 100
#    /
#   20


#
# Subcase 2: Node to be Deleted has One Child (Example: Deleting 30)
#
#     Search for the node to be deleted.
#     If the node has one child, delete the node and assign its child to its parent.


# Before Deletion (Leaf Node 30):
#          70
#        /    \
#       50     90
#      /  \    / \
#     30   60 80 100
#    /
#   20

# After Deletion (Leaf Node 30):
#   if we delete these 30 from here, 20 will become child of 50. So it's going to become the child of 50 as a left child

#          70
#        /    \
#       50     90
#      /  \    / \
#     20   60 80 100


#
# Subcase 3: Node to be Deleted has Two Children (Example: Deleting 70)
#
#     Find the successor of the node to be deleted (the minimum node in the right subtree).
#     Replace the node to be deleted with its successor.
#     Delete the successor node.

# Now, the successor of any given node is the minimum node, which is located at the right subtree. So we are going to look for the minimum node,
# which is located right subtree of this node over here in the right subtree. If you look at we can easily see that eighty over here is the minimum node.
# So this means that in the next step we are going to take 80 and update 80 to the place of the seventy over here, the note that we want to delete.
# Now, after updating, we can easily delete the 80 from this right subtree. So if we delete the eighty from this right subtree, we see that in this case
# eighty has one child. So this means that this child will become the child of eighties parent.

#   Before Deletion:

#          70
#        /    \
#       50     90
#      /  \    / \
#     30   60 80 100
#    / \       \
#   20  40      85

#   After Deletion 70:
#          80
#        /    \
#       50     90
#      /  \    / \
#     30   60 85 100
#    / \
#   20  40


# Case 2: Rotation is Required


# Subcase 1: Left-Left Condition (Example: Deleting 60)
#
#     Delete the node and check if its parent is unbalanced.
#     Identify it as a Left-Left condition.
#     Perform a right rotation on the unbalanced parent node.

#   Before Deletion:

#          70
#        /    \
#       50     90
#      /  \    / \
#     30   60 80 100
#    / \       \
#   20  40      85

#   After Deletion node 60: Imbalance

#          70
#        /    \
#       50     90
#      /       / \
#     30      80 100
#    / \       \
#   20  40      85

# Now, after deleting 60 from here, I'm going to check that if the parent of 60, which is 50, is this balanced or not?
# Now, in this case, we can easily see that this node over here is this balanced because the left subtree
# is height is two and the right subtree height is zero, and the difference between them is two.

#   The above is LEFT LEFT conditions of we do right rotation
#
# Now balanced after deletion

#          70
#        /    \
#       30     90
#      / \      / \
#     20 50    80 100
#                \
#                85


#
# Subcase 2: Left-Right Condition (Example: Deleting 100)
#
#     Delete the node and check if its parent is unbalanced.
#     Identify it as a Left-Right condition.
#     Perform a left rotation on the left child of the unbalanced parent and then a right rotation on the parent.

# Before deleting 100

#          80
#        /    \
#       50     90
#      /  \    / \
#     30   60 80 100
#    / \       \
#   20  40      85

# After deleting

#          80
#        /    \
#       50     90
#      /  \    /
#     30   60 80
#    / \       \
#   20  40      85

#   we see that 90 is displaced because left subtree hate of 90 is two and the rights of this hate is zero.
#   So the difference between them is two. So this means that this is this balance node. So in this case, after finding the balance node,
#   we need to identify the condition. Now To identify the condition, we are going to look for the path from 90 to its grandchild.
#   Now, in this case, we can easily see that it's left and right condition.

# Left rotation

#          80
#        /    \
#       50     90
#      /  \    /
#     30   60 85
#    / \       /
#   20  40    80

# Right rotation
#          80
#        /    \
#       50     85
#      /  \    / \
#     30   60 80 90
#    / \
#   20  40



#
# Subcase 3: Right-Right Condition (Deleting 30)
#
#     Delete the node and check if its parent is unbalanced.
#     Identify it as a Right-Right condition.
#     Perform a left rotation on the unbalanced parent node.

#          70
#        /     \
#       50      90
#      / \     /  \
#     30  60    80 100
#         \      \
#          70     85

# After deleting 30
#           70
#        /     \
#       50      90
#        \     /  \
#        60    80 100
#         \      \
#          70     85

# Now this is disbalanced... and right right condition. So we do left rotation
#          70
#        /    \
#       60     90
#      /  \    /  \
#     50  70   80 100
#                \
#                 85


#
# Subcase 4: Right-Left Condition (Example: Deleting 30)
#
#     Delete the node and check if its parent is unbalanced.
#     Identify it as a Right-Left condition.
#     Perform a right rotation on the right child of the unbalanced parent and then a left rotation on the parent.

#          70
#        /     \
#       50      90
#      / \     /  \
#     30  60   80 100
#         /      \
#        55      85
#   After deletion

#          70
#        /     \
#       50      90
#        \     /  \
#        60   80 100
#        /     \
#        55     85

# Right rotation

#          70
#        /     \
#       50      90
#        \     /  \
#        55   80 100
#         \     \
#         60     85

# Left Rotation

#          70
#        /     \
#       55      90
#      / \     /  \
#     55  60  80 100
#               \
#                85

