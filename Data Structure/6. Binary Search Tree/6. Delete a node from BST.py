#   Three Cases:
#
#     Leaf Node:
#         Directly delete the node.
#
#     One Child Node:
#         Deleting a node which has one child and make that child as parent node.
#
#     If not to be deleted has two Children Node:
#         Find the successor (minimum(the smallest node) value in the right subtree).
#         Replace the node's value with the successor's value.
#         Delete the successor.


class BSTNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


#   In the case 3, to find the successor we need to find the minimum node in the right subtree.
#   So we frst create min fuction

def minValueNode(bstNode):
    """
    Finds the node with the minimum value in the given Binary Search Tree.

    Parameters:
    - bstNode: The root node of the Binary Search Tree.

    Returns:
    - The node with the minimum value in the BST.
    """
    current = bstNode

    # Traverse to the leftmost child to find the minimum value node
    while current.leftChild is not None:  # We are using left because in BST we know that minimum value will be on left side
        current = current.leftChild

    return current


def deleteNode(rootNode, nodeValue):
    if rootNode is None:
        return rootNode  # Case: Node not found, return original tree

    # Case: Value to be deleted is smaller, move to the left subtree
    if nodeValue < rootNode.data:
        rootNode.left = deleteNode(rootNode.left, nodeValue)

    # Case: Value to be deleted is greater, move to the right subtree
    elif nodeValue > rootNode.data:
        rootNode.right = deleteNode(rootNode.right, nodeValue)

    # Case: Node to be deleted found
    else:
        # Case: Node has no child or only one child
        if rootNode.left is None:
            # If the left child is None, set temp to the right child
            temp = rootNode.right
            # Set the root node to None, effectively deleting it
            rootNode = None
            # Return the right child as the new root
            return temp

        elif rootNode.right is None:
            # If the right child is None, set temp to the left child
            temp = rootNode.left
            # Set the root node to None, effectively deleting it
            rootNode = None
            # Return the left child as the new root
            return temp

        # Case: Node has two children
        temp = minValueNode(rootNode.right)
        # Find the minimum value in the right subtree (successor)
        rootNode.data = temp.data
        # Replace the node's value with the successor's value
        rootNode.right = deleteNode(rootNode.right, temp.data)
        # Delete the successor
