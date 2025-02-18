class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary for children (links)
        self.end_of_string = False  # End-of-string property


class Trie:
    def __init__(self):
        self.root = TrieNode()  # Initialize root node


# Case 1: A Trie is Blank

#     Create nodes for each character in the string.
#     Set the end-of-string property for the last node.
#     Example: Inserting "APP" results in nodes for "A," "P," and "P," and next empty node with empty string with end of string True"

# APP
# _______________________________
# |        Dictionary            |
# |______________________________|
# | Character  | Link to Node    |
# |____________|_________________|
# |  A         |     ------------|---
# |______________________________|  |
# | END OF STRING = N            |  |
# |______________________________|  |
#                                   |
#                                   |
#                                  \ /
#                           _______________________________
#                            |        Dictionary            |
#                            |______________________________|
#                            | Character  | Link to Node    |
#                            |____________|_________________|
#                            |  P         |     ------------|---
#                            |______________________________|  |
#                            | END OF STRING = N            |  |
#                            |______________________________|  |
# #                                                             |
# #                                                             |
# #                                                            \ /
#                                                    _______________________________
#                                                    |        Dictionary            |
#                                                    |______________________________|
#                                                    | Character  | Link to Node    |
#                                                    |____________|_________________|
#                                                    |  P         |     ------------|---
#                                                    |______________________________|  |
#                                                    | END OF STRING = N            |  |
#                                                    |______________________________|  |
#                                                                                     \ /
#                                                                _______________________________
#                                                                |        Dictionary            |
#                                                                |______________________________|
#                                                                | Character  | Link to Node    |
#                                                                |____________|_________________|
#                                                                |            |                 |
#                                                                |______________________________|
#                                                                | END OF STRING = Y            |
#                                                                |______________________________|


#   CASE -2: Common Prefix in Trie:
#
#     If a new string shares a common prefix with an existing string, insert the remaining characters.
#     Example: Inserting "API" when "APP" is already in the Trie results in a new node for "I" with the end-of-string property set.


#   So in this case we see that A and P are common characters to this previous string that we created over here.
#   So this means that we will not insert A and P to this trie over here, because they are already exist.
#   Now, when we reach next node we see that I does not exist over here. So we know that in one node we can insert multiple characters.
#   So we will insert I. Now, after inserting I, we need to set that this is a string.
#   So we need to mention end of string parameter. So here again, we will create a new blank node, so in which

# API

# _______________________________
# |        Dictionary            |
# |______________________________|
# | Character  | Link to Node    |
# |____________|_________________|
# |  A         |     ------------|---
# |______________________________|  |
# | END OF STRING = N            |  |
# |______________________________|  |
#                                   |
#                                   |
#                                  \ /
#                           _______________________________
#                            |        Dictionary            |
#                            |______________________________|
#                            | Character  | Link to Node    |
#                            |____________|_________________|
#                            |  P         |     ------------|---
#                            |______________________________|  |
#                            | END OF STRING = N            |  |
#                            |______________________________|  |
# #                                                            |
# #                                                            |
# #                                                           \ /
#                                                    _______________________________
#                                                    |        Dictionary            |
#                                                    |______________________________|
#                                                    | Character  | Link to Node    |
#                                                    |____________|_________________|
#                                                    |  P         |     ------------|---
#                                                    |  I         |     ------------|-----------------------------------
#                                                    |______________________________|  |                                |
#                                                    | END OF STRING = N            |  |                                |
#                                                    |______________________________|  |                                |
#                                                                                     \ /                               |
#                                                                _______________________________                        |
#                                                                |        Dictionary            |                       |
#                                                                |______________________________|                       |
#                                                                | Character  | Link to Node    |             ___________________________
#                                                                |____________|_________________|             |        DICTIONARY        |
#                                                                |            |                 |             |__________________________|
#                                                                |______________________________|             |   Character |Link to Node|
#                                                                | END OF STRING = T            |             | ____________|____________|
#                                                                |______________________________|             |             |            |
#                                                                                                             |---------------------------
#                                                                                                             |     END OF STRING: T     |
#                                                                                                             |---------------------------
#
#
#
#
#
#


# CASE- 3: Prefix Already Present as a Complete String:
#
#     If the prefix of the new string is already present as a complete string, create a new node only for the remaining characters.
#     Example: Inserting "APIS" when "API" is already present only adds a new node for "S" with the end-of-string property set.

# APIS

# _______________________________
# |        Dictionary            |
# |______________________________|
# | Character  | Link to Node    |
# |____________|_________________|
# |  A         |     ------------|---
# |______________________________|  |
# | END OF STRING = N            |  |
# |______________________________|  |
#                                   |
#                                   |
#                                  \ /
#                           _______________________________
#                            |        Dictionary            |
#                            |______________________________|
#                            | Character  | Link to Node    |
#                            |____________|_________________|
#                            |  P         |     ------------|---
#                            |______________________________|  |
#                            | END OF STRING = N            |  |
#                            |______________________________|  |
# #                                                            |
# #                                                            |
# #                                                           \ /
#                                                    _______________________________
#                                                    |        Dictionary            |
#                                                    |______________________________|
#                                                    | Character  | Link to Node    |
#                                                    |____________|_________________|
#                                                    |  P         |     ------------|---
#                                                    |  I         |     ------------|-----------------------------------
#                                                    |______________________________|  |                                |
#                                                    | END OF STRING = N            |  |                                |
#                                                    |______________________________|  |                                |
#                                                                                     \ /                               |
#                                                                _______________________________                        |
#                                                                |        Dictionary            |                       |
#                                                                |______________________________|                       |
#                                                                | Character  | Link to Node    |             ___________________________
#                                                                |____________|_________________|             |        DICTIONARY        |
#                                                                |            |                 |             |__________________________|
#                                                                |______________________________|             |   Character |Link to Node|
#                                                                | END OF STRING = T            |             | ____________|____________|
#                                                                |______________________________|             |      S      |     -------|---
#                                                                                                             |---------------------------  |
#                                                                                                             |     END OF STRING: T     |  |
#                                                                                                             |---------------------------  |
#                                                                                   --------------------------------------------------------|
#                                                                                  \/
#                                                                _______________________________
#                                                                |        Dictionary            |
#                                                                |______________________________|
#                                                                | Character  | Link to Node    |
#                                                                |____________|_________________|
#                                                                |            |                 |
#                                                                |______________________________|
#                                                                | END OF STRING = T            |
#                                                                |______________________________|
#
#
#


#   CASE: 4. String Already Present in Trie:
#
#     If the entire string is already in the Trie, no new nodes are inserted.
#     Example: Inserting "APIS" again, when "APIS" is already present, does not result in new nodes.


class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False


class Trie:
    def __init__(self):
        self.root = TrieNode()  # Initialize root node

    def insertString(self, word):
        current = self.root  # Start from the root node
        for char in word:
            charc = char  # Store the current character for clarity
            node = current.children.get(charc)  # Check if the character exists in the current node's children
            if node is None:
                # If the character does not exist, create a new TrieNode
                node = TrieNode()
                # Update the current node's children with the new character and its corresponding TrieNode
                current.children.update({charc: node})
            current = node  # Move to the next node in the Trie
        current.endOfString = True  # Set the endOfString property of the last node to True, indicating the end of the word
        print("Successfully Inserted")


newTrie = Trie()
newTrie.insertString("App")
