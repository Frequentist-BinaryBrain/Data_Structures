#   Creation of Binary Tree using Linked List:
#
#     We defined a TreeNode class representing a node in the binary tree.
#     Each node has three components: data, left child, and right child.
#     The creation of the binary tree involves initializing an object of the TreeNode class, designating the root node.

class TreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

newBT = TreeNode("Drinks") #  -------> O(1)


#   Time and Space Complexity:
#
#     Time Complexity: O(1) - Constant time as we are initializing a single object.
#     Space Complexity: O(1) - Constant space as only one node is being created.
#
# Importance of Learning Traversal Early:
#
#     Traversal is introduced early as it is heavily used in the insertion process.
#     Learning traversal first provides a foundation for understanding and implementing subsequent operations.
