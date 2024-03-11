#  Let's say we have 30,25,35,20,15,5,10,50,60,70, 65, and we want to insert these in to AVL tree

#   every time after adding new node, we are checking that if this AVL tree is balanced or not.

# Step 1: Insert 30
# Step 2: Insert 25

#      30
#     /
#    25

# Step 3: Insert 35

#      30
#     /  \
#    25  35

# Step 4: Insert 20
#      30
#     /  \
#    25  35
#   /
#  20

# Step 5: Insert 15
#      30
#     /  \
#    25  35
#   /
#  20
#  /
# 15

#  So in this case, we see that 25 is not balanced. Because the height of left subtree is two and the height of right subtree is zero
#  and the difference between them is 2. So this means that this node over here is not balanced. So after finding that this node is not balanced,
#  the next thing that we need to do, we need to find which condition is this. So to find the condition, we will find the path to the grandchild of this node.
#  So the grandchild of this node is 15. So the path to the 15 is left and the left. So this means that this is left left condition. So we know that in case
#  of left left condition, we need to do the right rotation of imbalanced node. So we have to do for this disbalanced the right rotation.

#      30
#     /  \
#    20  35
#   / \
#  15  25

# Step 6: Insert 5
#       30
#      /  \
#     20  35
#    / \
#   15  25
#  /
#  5

#   So if we check this node, 15 is balanced, 20 is balanced. But if we check 30, 30 is disbalanced. Because this child's height is three and the right child's
#   height is one. So the difference between them is two. So this node over here is disbalanced. So we need to find out which condition is this.
#   So to find out the condition, we need to find the path to the grandchild. So in this case, we see that we have two grandchild and the height 15 is greater
#   than the height of 25. So this means that we will take this grandchild. So the path to this grandchild is left and left.
# So this means that this is left left condition. So in case of left left condition, we are doing the right rotation.

#         20
#        /  \
#      15    30
#     /      / \
#    5      25 35

# Step 7: Insert 10
#         20
#        /  \
#      15    30
#     /      / \
#    5      25 35
#     \
#      10

#   So after adding this, we see that 15 becomes disbalanced. So because the left subtree's height is two and right subtree's height is zero and
#   difference between them is two. Now, in this case, we need to find out that which condition is this. So to find the condition we need to
#   find out the path to the grandchild. So it will be left and right. So this means that this is left right condition. Now in case of left right condition,
#   as the name implies, first, we have to do left rotation, then we have to do right rotation. But we need to take into account that we are doing
#   left rotation for the left child of this disbalanced node over here. Now, in our case, the left child is five. So we need to do left rotation for
#   this node over here. So if we do the left rotation for five, 10 will come up and five will be the left child of 10 over here. So after doing this,
#   this becomes left left condition.

#         20
#        /  \
#      15    30
#     /      / \
#    10      25 35
#    /
#   5

#   So in case of left left condition, we know that we have to do right rotation for disbalanced node.
# #   Now, if we do the right rotation, 15 comes down and ten goes to the place of 15 and 15 becomes the right child of 10.
# #   Now with this, we have made our tree balanced. Now we'll continue to the next case.

#          20
#        /   \
#      10     30
#     / \     / \
#    5  15   25 35

# Step 8: Insert 50
#          20
#        /   \
#      10     30
#     / \     / \
#    5  15   25 35
#                 \
#                 50

#   Now, after adding this if we check all nodes, we see that this tree is still balanced.So we don't need to do any rotation over here.

# Step 9: Insert 60
#          20
#        /   \
#      10     30
#     / \     / \
#    5  15   25 35
#                 \
#                 50
#                   \
#                   60

#   So after adding sixty as a right child 50, we see that 35 becomes disbalanced. So in this case, we need to identify which condition is this.
#   So to identify the condition, we need to find out the path to the grandchild So in this case, we see that the path is right and right.
#   So this means that this is right right condition. And we have learned that in case of right right condition, we need to do left rotation for the
#   disbalanced node. So if we do the left rotation for this 35 over here, 35 will come down and 50 will be
#   the place of 35 and the 35 will be the left child of 50.
#   So with this we made our tree balanced

#         20
#        /  \
#      10    30
#     / \    / \
#    5  15  25 50
#              / \
#             35  60

# Step 10: Insert 70
#         20
#        /  \
#      10    30
#     / \    / \
#    5  15  25 50
#              / \
#             35  60
#                   \
#                   70


#   After adding this, if we check all nodes, we see that 30 becomes disbalanced node. Because the height of 30 for the right subtree is three and for
#   the left subtree is one. So the difference between them is two. So this means that 30 is disbalanced. So the next thing that we need to do, we need to
#   identify which case is this. So we need to find a path to the grandchild of 30. Now, in this case, you see that we have two grandchild for the thirty.
#   So, as always, we need to take the one which is big height. So in this case, sixty's height is bigger than thirty five. So we need to find out path to the 60.
#   So in this case, it is right right. So this is one more time right right condition.
#   So in case of right right condition we know that we have to do left rotation. So if we do the left rotation for 30, 30 will come up with the 25 and 50 will come to the place of
#   30 with its children. And 35, the left child of 50 will be the right child of thirty over here. So with this we have made our tree balanced.

#          20
#        /   \
#      10     50
#     / \    /  \
#    5  15  30  60
#           / \   \
#          25 35   70
#


# Step 11: Insert 65


#          20
#        /   \
#      10     50
#     / \    /  \
#    5  15  30  60
#           / \   \
#          25 35   70
#                 /
#                65


#   we see that 60 becomes disbalanced node. So we need to find out which condition is this. So to find the condition one more time we will find the path
#   to the grandchild. So in this case, it's right and left. So this means that this is right left condition. As the name implies, in case of right left
#   condition first we need to do right rotation, then left rotation. But here you need to take into account that we are doing the right rotation for the
#   right child of disbalanced node. This means that we will do right rotation for seventy over here. So if we do the right rotation for seventy,
#   sixty five becomes the place of 70 and 70 becomes the right child of 65. So after doing so, we see that disbalance of 60 becomes right right condition.


#          20
#        /   \
#      10     50
#     / \    /  \
#    5  15  30  60
#           / \   \
#          25 35   65
#                   \
#                    70

#   So in case of right right condition, we are doing left rotation. So if we do the left rotation for 60 over here, 60 becomes down and
#   sixty five becomes the root of 60 and 60 becomes the left child of 65. So with this we have made our tree balanced.

#          20
#        /   \
#      10     50
#     / \    /   \
#    5  15  30    65
#           / \   / \
#          25 35 60 70

