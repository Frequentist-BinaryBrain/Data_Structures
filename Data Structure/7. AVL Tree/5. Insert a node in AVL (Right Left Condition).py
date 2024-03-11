

#   Handling Right-Left (RL) Condition:
#
#     Right Rotation for Right Child:
#     Left Rotation for Disbalanced Node:

#
#          50
#        /   \
#       40    60
#               \
#                70


# Insert 65 node

#          50
#        /   \
#       40    60
#               \
#                70
#                /
#               65

#     Right Rotation for Right Child:

#          50
#        /   \
#       40    60
#               \
#                65
#                  \
#                   70

#     Left Rotation for Disbalanced Node:

#          50
#        /   \
#       40    65
#            /  \
#           60   70


#    Algorithm of RIGHT LEFT Condition

# Step - 1: Rotate disbalancedNode.Rightchild
# Step - 2: Rotate LEft disbalanced Node

# Step - 1

# Step - 1: Rotate disbalancedNode.Rightchild
def rotateRight(disbalancedNode):
    # Store the right child of disbalancedNode
    newRoot = disbalancedNode.leftChild

    # Update the right child of disbalancedNode to be the left child of newRoot
    disbalancedNode.leftChild = newRoot.rightChild

    # Set the left child of newRoot to be the original disbalancedNode
    newRoot.rightChild = disbalancedNode
    # update height of disbalancedNode and newRoot
    return newRoot


# Step - 2
# Step - 2: Rotate Left disbalanced Node
def rotateLeft(disbalancedNode):
    # Store the left child of disbalancedNode
    newRoot = disbalancedNode.RightChild

    # Update the left child of disbalancedNode to be the right child of newRoot
    disbalancedNode.RightChild = newRoot.leftChild

    # Set the right child of newRoot to be the original disbalancedNode
    newRoot.leftChild = disbalancedNode

    # update height of disbalancedNode and newRoot
    return newRoot
