#   A Binary Search Tree (BST) is created using linked lists, and various operations can be performed on it.
#
# Common Operations on BST:
#
#     Creation of Binary Search Tree
#     Insertion of a Node
#     Deletion of a Node
#     Searching for a Value
#     Traversing All Nodes
#     Deletion of Entire BST
#
# Creating a Binary Search Tree

class BSTNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


newBST = BSTNode(None)  # -------------> O(1)
