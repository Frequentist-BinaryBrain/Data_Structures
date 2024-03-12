#   Common Operations on Binary Heap:
#
#     Creation of binary heap
#     Peek the top of the binary heap
#     Extract the minimum or maximum from the binary heap
#     Traversal of the binary heap (Level Order Traversal is discussed)
#     Size of the binary heap
#     Insert a value in the binary heap
#     Delete the entire binary heap

#   Implementation Options for Binary Heap:
#
#     Two options: Array or List, Reference or Pointer
#     Array-based implementation is chosen for its suitability with binary heaps.


# We will use Array implementation for Binary Heap

# Using an array for binary heap implementation is advantageous due to:
#
#     Memory Efficiency: Arrays utilize memory more effectively.
#     Simplicity: Indexing and access are straightforward.
#     Cache Locality: Sequential storage enhances cache performance.
#     Random Access: Allows constant-time access to elements.
#     Level Order Traversal: Aligns well with array storage.
#     Space Efficiency: Minimizes overhead, storing only necessary data.
#     Insertion and Deletion Efficiency: Swapping elements is straightforward.
#     Predictable Indexing: Supports predictable and consistent indexing.
#     Support for Heap Properties: Aligns naturally with heap property conditions.
#     Optimal Space Usage: Allows dynamic resizing for optimal space utilization.


# IMPORTANT
# Array Implementation of Binary Heap:

# The binary heap is stored in memory using a Python list or an array.
# The root node is at index 1, and left and right children are calculated using specific formulas.
# Index calculations are done as follows:
#     Left child index = 2 * parent index
#     Right child index = 2 * parent index + 1

#  Binary Heap:
#     10
#    /  \
#   20   30
#  / \   /
# 40 50 60

#   Index:  1  2  3  4  5  6
#  Array: [10,20,30,40,50,60]

#   In this example:
#
#     The root node (10) is at index 1.
#     The left child of 10 is calculated as 2 * 1 = 2, and the right child is 2 * 1 + 1 = 3.
#     The left child of 20 is 2 * 2 = 4, and the right child is 2 * 2 + 1 = 5.
#     The left child of 30 is 2 * 3 = 6.


#   Creation of Binary Heap:
#
#     A fixed-size Python list is created based on user input.
#     Heap size is initialized to zero.
#     Maximum size is set to size + 1, ignoring index zero.
#     Time complexity: O(1), Space complexity: O(n)

class BinaryHeap:
    def __init__(self, size):
        # Create a fixed-size Python list based on user input
        self.custom_list = (size + 1) * [None]
        # Initialize heap size to zero
        self.heap_size = 0
        # Set maximum size to size + 1, ignoring index zero
        self.max_size = size + 1


# Peek Operation:
#
#     Returns the value of the root node without removing it.
#     Implemented by accessing the value at index 1 in the list.
#     Time complexity: O(1), Space complexity: O(1)

def peek_of_heap(root_node):
    """
    Peek at the value of the root node in a binary heap.

    Parameters:
    - root_node: The root node of the binary heap.

    Returns:
    - The value of the root node, or None if the heap is empty.
    """
    if root_node:
        # If the root node exists, return the value at index 1 in the custom_list
        return root_node.custom_list[1]
    else:
        # If the root node is None, the heap is empty, return None
        return None


#   Size of Binary Heap:
#
#     Returns the number of elements in the heap (filled cells).
#     Time complexity: O(1), Space complexity: O(1)


def sizeofHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.heap_size


# Traversal of Binary Heap (Level Order Traversal):
#
#     Iterates through filled cells of the custom list from left to right, level by level.
#     Time complexity: O(n), Space complexity: O(1)

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        for i in range(1, rootNode.heap_size + 1):
            print(rootNode.customList[i])

