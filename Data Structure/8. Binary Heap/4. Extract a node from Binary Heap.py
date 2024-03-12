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
    parentIndex = int(index / 2)
    if index <= 1:
        return
    if heapType == "Min":
        if rootNode.custom_list[index] < rootNode.custom_list[parentIndex]:
            temp = rootNode.custom_list[index]
            rootNode.custom_list[index] = rootNode.custom_list[parentIndex]
            rootNode.custom_list[parentIndex] = temp
        heapifyTreeInsert(rootNode, parentIndex, heapType)
    elif heapType == "Max":
        if rootNode.custom_list[index] > rootNode.custom_list[parentIndex]:
            temp = rootNode.custom_list[index]
            rootNode.custom_list[index] = rootNode.custom_list[parentIndex]
            rootNode.custom_list[parentIndex] = temp
        heapifyTreeInsert(rootNode, parentIndex, heapType)


def insertNode(rootNode, nodeValue, heapType):
    if rootNode.heap_size + 1 == rootNode.max_size:
        return "The Binary heap is full"
    rootNode.custom_list[rootNode.heap_size + 1] = nodeValue
    rootNode.heap_size += 1
    heapifyTreeInsert(rootNode, rootNode.heap_size, heapType)
    return "The value is successfully inserted"


#   Extracting an Element from Binary Heap:
#
#     Root Node Extraction:
#         In a binary heap, only the root node can be extracted.
#         Extraction involves promoting other elements to maintain the heap property.
#
#     Adjustments after Extraction:
#         Find the last element in the heap and replace it with the root node.
#         Adjust the heap to maintain the heap property.
#
#     Heapify Tree Extract Method:
#         Parameters: rootNode, index, heapType.
#         Calculates left and right child indices.
#         Handles cases based on the number of children (none, one, or two).
#         Swaps elements based on heap type (min or max).
#         Recursively calls the method for further adjustments.
#
#     Extract Node Method:
#         Parameters: rootNode, heapType.
#         Checks if the heap is empty and returns if so.
#         Extracts the root node, replaces it with the last node, and adjusts the heap.
#         Calls the heapifyTreeExtract method.
#         Returns the extracted node.

#       5
#      /  \
#     10   20
#    / \   / \
#   30 40 50 60
#  /
# 80

# Index: 1  2    3  4   5   6   7  8
# LIST:  5, 10, 20, 30, 40, 50, 60 80

# As we mentioned, we can extract only root node. So in this case, we will extract five from here. But the problem over here is right now that,
# if we extract 5 from here, we will not have root node. So we need to do some adjustment to set root node over here.
# Now, in this case, the first step that we will do, we will find the last element from the binary heap. So the last element in our case is the one
# which is located at the last level, it should be on the right. So in this case, at the last level, we have only one element.
#  So the last element will be 80 in this case

#   So after finding this, we will replace this element with the root node.

#       80
#      /  \
#     10   20
#    / \   / \
#   30 40 50 60

#   but we have a problem over here. So the problem is, after replacing this, we see that binary heap property is violated, which says that
#  in the case of minimum binary heap, the root must be less than the children. But in this case, you see that the root is greater than its children.
#  Now, to solve this problem, we will promote one of the children of this node, its place, and replace the root node. We need to decide which child to
#  promote, left or right child. So here this is a minimum heap. So we will select the child, which is smaller. So in this case, the smaller child is 10.
#  So we will swap 10 with 80.

#       10
#      /  \
#     80   20
#    / \   / \
#   30 40 50 60

#   Now, one more time, we need to swap one of child with this root node over here.

#       10
#      /  \
#     30   20
#    / \   / \
#   80 40 50 60

# Index: 1    2   3  4   5   6   7
# LIST:  10, 30, 20, 80, 40, 50, 60

#   you see that all roots are smaller than its children.


def heapifyTreeExtract(rootNode, index, heapType):
    # Calculate the indices of the left and right child nodes
    leftIndex = index * 2
    rightIndex = index * 2 + 1
    swapChild = 0  # Initialize the variable to track the child node to be swapped

    # Check if the left child index is beyond the heap size
    if rootNode.heap_size < leftIndex:
        return
    # Check if there is only a left child for the current node
    elif rootNode.heap_size == leftIndex:
        # Adjust the heap for a minimum heap if needed
        if heapType == "Min":
            if rootNode.custom_list[index] > rootNode.custom_list[leftIndex]:
                temp = rootNode.custom_list[index]
                rootNode.custom_list[index] = rootNode.custom_list[leftIndex]
                rootNode.custom_list[leftIndex] = temp
            return
        # Adjust the heap for a maximum heap if needed
        else:
            if rootNode.custom_list[index] < rootNode.custom_list[leftIndex]:
                temp = rootNode.custom_list[index]
                rootNode.custom_list[index] = rootNode.custom_list[leftIndex]
                rootNode.custom_list[leftIndex] = temp
            return
    # Case where the current node has both left and right children
    else:
        # Determine which child node to swap based on the heap type
        if heapType == "Min":
            if rootNode.custom_list[leftIndex] < rootNode.custom_list[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            # Swap the current node with the smaller child
            if rootNode.custom_list[index] > rootNode.custom_list[swapChild]:
                temp = rootNode.custom_list[index]
                rootNode.custom_list[index] = rootNode.custom_list[swapChild]
                rootNode.custom_list[swapChild] = temp
        else:
            if rootNode.custom_list[leftIndex] > rootNode.custom_list[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            # Swap the current node with the larger child
            if rootNode.custom_list[index] < rootNode.custom_list[swapChild]:
                temp = rootNode.custom_list[index]
                rootNode.custom_list[index] = rootNode.custom_list[swapChild]
                rootNode.custom_list[swapChild] = temp

        # Recursively call heapifyTreeExtract on the swapped child
        heapifyTreeExtract(rootNode, swapChild, heapType)


def extractNode(rootNode, heapType):
    # Check if the heap is empty
    if rootNode.heap_size == 0:
        return
    else:
        # Extract the root node value
        extractedNode = rootNode.custom_list[1]
        # Replace the root node with the last node
        rootNode.custom_list[1] = rootNode.custom_list[rootNode.heap_size]
        rootNode.custom_list[rootNode.heap_size] = None
        rootNode.heap_size -= 1
        # Adjust the heap after extraction
        heapifyTreeExtract(rootNode, 1, heapType)
        return extractedNode


# Creating a new binary heap with a max size of 5
newHeap = BinaryHeap(5)
# Inserting elements into the heap
insertNode(newHeap, 4, "Max")
insertNode(newHeap, 5, "Max")
insertNode(newHeap, 2, "Max")
insertNode(newHeap, 1, "Max")
insertNode(newHeap, 14, "Max")
# Extracting the root node from the heap with max heap property
print(extractNode(newHeap, "Max"))
