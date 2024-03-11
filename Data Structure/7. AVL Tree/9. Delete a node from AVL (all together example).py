#   Say I have below AVL tree

#          70
#        /    \
#       50      90
#      /  \     / \
#     30   60  80 100
#    / \    \       \
#   20  40   65     110
#  /
# 15


# DELETE 40

#          70
#        /    \
#       50      90
#      /  \     / \
#     30   60  80 100
#    /      \       \
#   20      65       110
#  /
# 15

#   Now, if I delete 40 from here. You can easily see that the parent of 40 i.e 30 becomes imbalance because the left subtree height is two
#   and the right subtree height is  zero.

# Now, after finding imbalance note, we need to find the condition of this node so we can easily
# see that this is left left condition because the path from 30 to 15 it is left left.

# Now do Right rotation since it is left left condition

# Right Rotation
#          70
#        /    \
#       50      90
#      /  \     / \
#     20   60  80 100
#    / \     \      \
#   15  30    65     110

# DELETE 15

#          70
#        /    \
#       50      90
#      /  \     / \
#     20   60  80 100
#      \     \      \
#      30    65      110

# Here tree is balanced after removing 15, so no need any rotation

# DELETE 65

#          70
#        /    \
#       50      90
#      /  \     / \
#     20   60  80 100
#      \            \
#      30            110

# Here tree is balanced after removing 65, so no need any rotation

# DELETE 60

#          70
#        /    \
#       50      90
#      /        / \
#     20       80 100
#      \            \
#      30            110

# We can now see that parent of 60 i.e 50 is imbalanced
# This is left Right condition because from parent 50 to grandchild 30 is left and then right

# So in case of left right condition, we know that first we are doing left rotation, then we are doing right rotation.
# So here we are doing left rotation for the left child of this imbalanced node, which is 20.
# So this means that we are going to do left rotation for 20 over here.

# Left rotation
#          70
#        /    \
#       50      90
#      /        / \
#     30       80 100
#     /             \
#    20              110

# Right rotation
#          70
#        /    \
#       30      90
#      / \      / \
#     20  50   80 100
#                   \
#                    110

