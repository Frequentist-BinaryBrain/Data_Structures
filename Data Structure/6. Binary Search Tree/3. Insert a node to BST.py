#   Binary Search Tree (BST) - Node Insertion:
#     Inserting a node into a Binary Search Tree involves traversing the tree based on comparisons with the node values.
#
#     Two cases:
#         If the BST is empty (root node is None), a new node is created, and the value is assigned to the root.
#         If the BST has nodes, traverse the tree:
#             If the value to be inserted is less than the current node, move to the left subtree.
#             If the value is greater, move to the right subtree.
#             Repeat until an empty spot is found, then insert the new node.


class BSTNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insertNode(rootNode, nodeValue):

    """
    Inserts a node with the given value into the Binary Search Tree.

    Parameters:
    - rootNode: The root node of the Binary Search Tree.
    - nodeValue: The value to be inserted into the BST.

    Returns:
    - A message indicating that the node has been successfully inserted.
    """
    
    # Case 1: If the BST is empty (root node is None), create a new node and assign the value to the root.
    if rootNode.data is None:
        rootNode.data = nodeValue
    # Case 2: If the value to be inserted is less than the current node, move to the left subtree.
    elif nodeValue < rootNode.data:
        # If the left child is None, create a new node and assign it as the left child.
        if rootNode.left is None:
            rootNode.left = BSTNode(nodeValue)
        # If the left child exists, recursively call insertNode for the left subtree.
        else:
            insertNode(rootNode.left, nodeValue)
    # Case 3: If the value to be inserted is greater than or equal to the current node, move to the right subtree.
    else:
        # If the right child is None, create a new node and assign it as the right child.
        if rootNode.right is None:
            rootNode.right = BSTNode(nodeValue)
        # If the right child exists, recursively call insertNode for the right subtree.
        else:
            insertNode(rootNode.right, nodeValue)

    return "Node has been successfully inserted"


newBT = BSTNode(None)
print(insertNode(newBT, 70))
print(insertNode(newBT, 10))
print(insertNode(newBT, 80))
print(newBT.left.data)
print(newBT.right.data)
