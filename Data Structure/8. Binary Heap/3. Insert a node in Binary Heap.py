#   Overview of Binary Heap Insertion Process:
#
#     Finding the Empty Cell:
#         In a complete binary heap, nodes are filled from left to right, top to bottom.
#         The first step is to find the first unused cell. This is typically the leftmost empty cell in the last level of the heap.
#
#     Inserting the Node:
#         Place the new node in the found empty cell.
#
#     Restoring Heap Property:
#         After insertion, check if the heap property is violated.
#         If violated, swap the node with its parent until the heap property is restored.
#         This process involves comparing the node with its parent and swapping if necessary.
#
#     Heapify Method:
#         The heapify method is introduced to handle the adjustment process after insertion.
#         It takes the root node, the index of the node to adjust, and the heap type as parameters.
#         The method recursively compares the node with its parent and swaps if needed, ensuring the heap property is maintained.


# Example Minimum Heap

#     5
#    /  \
#   10   20
#  / \   / \
# 30 40 50 60

# Index: 1  2    3  4   5   6   7
# LIST:  5, 10, 20, 30, 40, 50, 60

# Insert 1

#      5
#     /  \
#    10   20
#   / \   / \
#  30 40 50 60
#  /
# 1

# Index: 1  2    3  4   5   6   7  8
# LIST:  5, 10, 20, 30, 40, 50, 60 1

# So after inserting one over here, we see that we have a problem over here. So the problem is main property of binary heap
# in the case of minimum heap, which says that the root is always less than the left and right child.
# But in this case, we see that root 30 is bigger than 1.

#   We'll just replace one with 30 and 30 will come down to the place of one. So we will replace them in the list also.

#        5
#      /  \
#     10   20
#    / \   / \
#   1  40 50 60
#  /
# 30

# Index: 1  2    3  4   5   6   7   8
# LIST:  5, 10, 20, 1, 40, 50,  60  30

# Again 10 is greater than 1, so we will push it down

#        5
#      /  \
#     1    20
#    / \   / \
#  10  40 50 60
#  /
# 30

# Index: 1  2   3  4   5   6   7   8
# LIST:  5, 1, 20, 10, 40, 50,  60  30

# Now 5

#        1
#      /  \
#     5    20
#    / \   / \
#  10  40 50 60
#  /
# 30

# Index: 1  2   3  4   5   6   7   8
# LIST:  1, 5, 20, 10, 40, 50,  60  30

# This process if done by heapify: Heapify Method:
# #         The heapify method is introduced to handle the adjustment process after insertion.
# #         It takes the root node, the index of the node to adjust, and the heap type as parameters.
# #         The method recursively compares the node with its parent and swaps if needed, ensuring the heap property is maintained.


class BinaryHeap:
    def __init__(self, size):
        self.custom_list = (size + 1) * [None]
        self.heap_size = 0
        self.max_size = size + 1


def peek_of_heap(root_node):
    if root_node:
        return root_node.custom_list[1]
    else:
        return None


def sizeofHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.heap_size


def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        for i in range(1, rootNode.heap_size + 1):
            print(rootNode.custom_list[i])


def heapifyTreeInsert(rootNode, index, heapType):
    # Calculate the parent index using integer division
    parentIndex = int(index / 2)

    # Base case: if the index is less than or equal to 1, return
    if index <= 1:
        return

    # Check heap type for Min Heap
    if heapType == "Min":
        # Compare the current node with its parent, swap if needed
        if rootNode.custom_list[index] < rootNode.custom_list[parentIndex]:
            temp = rootNode.custom_list[index]
            rootNode.custom_list[index] = rootNode.custom_list[parentIndex]
            rootNode.custom_list[parentIndex] = temp
        # Recursively call heapifyTreeInsert on the parent index
        heapifyTreeInsert(rootNode, parentIndex, heapType)

    # Check heap type for Max Heap
    elif heapType == "Max":
        # Compare the current node with its parent, swap if needed
        if rootNode.custom_list[index] > rootNode.custom_list[parentIndex]:
            temp = rootNode.custom_list[index]
            rootNode.custom_list[index] = rootNode.custom_list[parentIndex]
            rootNode.custom_list[parentIndex] = temp
        # Recursively call heapifyTreeInsert on the parent index
        heapifyTreeInsert(rootNode, parentIndex, heapType)


def insertNode(rootNode, nodeValue, heapType):
    # Check if the binary heap is full
    if rootNode.heap_size + 1 == rootNode.max_size:
        return "The Binary heap is full"

    # Insert the new node value at the next available index
    rootNode.custom_list[rootNode.heap_size + 1] = nodeValue

    # Increase the heap size
    rootNode.heap_size += 1

    # Call heapifyTreeInsert to maintain the heap property
    heapifyTreeInsert(rootNode, rootNode.heap_size, heapType)

    return "The value is successfully inserted"


newHeap = BinaryHeap(5)
insertNode(newHeap, 4, "Max")
insertNode(newHeap, 5, "Max")
insertNode(newHeap, 2, "Max")
insertNode(newHeap, 1, "Max")
insertNode(newHeap, 14, "Max")
levelOrderTraversal(newHeap)
