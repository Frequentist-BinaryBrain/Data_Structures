#             N1
#            /  \
#          N2   N3
#         / \   / \
#        N4 N5 N6 N7
#              |
#             N8

#   In postOrder traversal, we visit the left subtree first, then the right subtree, and finally the root node. For our example:
#
# So, the postOrder traversal sequence is N4, N5, N2, N8, N6, N7, N3, N1.


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

newBT = TreeNode("Drinks")
leftChild = TreeNode("hot")
rightChild = TreeNode("cold")
newBT.left = leftChild
newBT.right = rightChild

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.left)
    preOrderTraversal(rootNode.right)

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.left)
    print(rootNode.data)
    inOrderTraversal(rootNode.right)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.left)
    postOrderTraversal(rootNode.right)
    print(rootNode.data)

# Testing the traversals
print("PreOrder Traversal:")
preOrderTraversal(newBT)

print("\nInOrder Traversal:")
inOrderTraversal(newBT)

print("\nPostOrder Traversal:")
postOrderTraversal(newBT)



