#       Creation of Trie Data Structure:
#         To create a Trie, initialize a blank root node.
#         Each node logically contains characters and links to child nodes.
#         Physically, a node may include characters, links (references to children), and an end-of-string property.
#
#     Implementation of Trie Node Class:
#         Two classes are created: TrieNode and Trie.
#         TrieNode class includes a dictionary for children (to establish links) and an end-of-string property.
#         Initialization sets end-of-string to false by default.
#
#     Implementation of Trie Class:
#         Trie class is created, initializing the root node using the TrieNode class.
#         Root node is a blank node without assigned values.
#         Initializing an instance of the Trie class creates a new Trie.


class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary for children (links)
        self.end_of_string = False  # End-of-string property


class Trie:
    def __init__(self):
        self.root = TrieNode()  # Initialize root node

    #   In the Trie data structure, the root node serves as the entry point and foundation of the entire Trie.
    #   By initializing an instance of the Trie class and assigning the root attribute to a TrieNode instance,
    #   you establish the starting point for building the Trie.

# Creating a new Trie
new_trie = Trie()


