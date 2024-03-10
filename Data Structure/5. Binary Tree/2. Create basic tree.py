# Definition of a TreeNode class
class TreeNode:
    # Constructor to initialize a TreeNode with data and children (defaulted to an empty list)
    def __init__(self, data, children=[]):
        self.data = data
        self.children = children

    # String representation of the TreeNode, used for printing the tree structure
    def __str__(self, level=0):
        # Create an indented string representation with the data at the current level
        ret = " " * level + str(self.data) + "\n"
        # Recursively add string representations of each child, with increased indentation level
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

    # Method to add a child TreeNode to the current node
    def addChild(self, TreeNode):
        self.children.append(TreeNode)


# Creating a tree with 'Drinks' as the root
tree = TreeNode('Drinks',
                [])  # data is drinks over here, it becomes the value of the data attribute for the newly created TreeNode instance.

# Creating child nodes for 'Drinks': 'cold' and 'hot'
cold = TreeNode('cold', [])
hot = TreeNode('hot', [])

# Adding 'cold' and 'hot' as children to the 'Drinks' node
tree.addChild(cold)
tree.addChild(hot)

# Creating child nodes for 'cold': 'Cola' and 'Fanta'
tea = TreeNode('Tea', [])
coffee = TreeNode('coffee', [])
cola = TreeNode('Cola', [])
fanta = TreeNode('Fanta', [])

# Adding 'Cola' and 'Fanta' as children to the 'cold' node
cold.addChild(cola)
cold.addChild(fanta)

# Adding 'Tea' and 'Coffee' as children to the 'hot' node
hot.addChild(tea)
hot.addChild(coffee)

# Printing the entire tree structure
print(tree)

#  When you want to add child nodes together


#   # Definition of a TreeNode class
# class TreeNode:
#     # Constructor to initialize a TreeNode with data and children (defaulted to an empty list)
#     def __init__(self, data, *children):
#         self.data = data
#         self.children = list(children)
#
#     # String representation of the TreeNode, used for printing the tree structure
#     def __str__(self, level=0):
#         # Create an indented string representation with the data at the current level
#         ret = " " * level + str(self.data) + "\n"
#         # Recursively add string representations of each child, with increased indentation level
#         for child in self.children:
#             ret += child.__str__(level + 1)
#         return ret
#
#     # Method to add a child TreeNode to the current node
#     def addChild(self, TreeNode):
#         self.children.append(TreeNode)
#
#
# # Creating a tree with 'Drinks' as the root
# tree = TreeNode("Drinks",
#                 TreeNode('cold', TreeNode('Fanta', TreeNode("250ml")), TreeNode('Cola'), TreeNode("Sprite")),
#                 TreeNode('hot', TreeNode('coffee'), TreeNode('Tea'), TreeNode('Milk')))
#
# # Printing the entire tree structure
# print(tree)
