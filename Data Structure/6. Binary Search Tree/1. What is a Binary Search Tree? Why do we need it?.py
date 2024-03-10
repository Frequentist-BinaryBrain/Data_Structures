#   Binary Search Tree (BST) is a type of binary tree with additional properties.
#
# Properties:
#
#     In the left subtree, the value of a node is less than or equal to its parent node's value.
#     In the right subtree, the value of a node is greater than its parent node's value.
#
# Example:
#     If we have a BST with the root node as 70:
#         In the left subtree, values are less than or equal to 70.
#         In the right subtree, values are greater than 70.
#         This property is recursively applied to all subtrees.

#              70
#             /  \
#            50   90
#           / \   / \
#          30  60 80 100
#         / \
#        20  40
#   Why BST:
#
#     BST does not store an index of its data elements.
#     It relies on implicit structure for fast insertion and deletion.
#     The structure allows us to traverse only a fraction of the tree, making operations faster than linear traversal.
#
# Performance:
#
#     Insertion and deletion of nodes in BST are achieved more quickly compared to linear structures.
#     Instead of sequentially traversing every element, BST allows us to traverse only a portion of the tree, enhancing efficiency.
