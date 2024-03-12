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


def heapifyTreeExtract(rootNode, index, heapType):
    leftIndex = index * 2
    rightIndex = index * 2 + 1
    swapChild = 0

    if rootNode.heap_size < leftIndex:
        return
    elif rootNode.heap_size == leftIndex:
        if heapType == "Min":
            if rootNode.custom_list[index] > rootNode.custom_list[leftIndex]:
                temp = rootNode.custom_list[index]
                rootNode.custom_list[index] = rootNode.custom_list[leftIndex]
                rootNode.custom_list[leftIndex] = temp
            return
        else:
            if rootNode.custom_list[index] < rootNode.custom_list[leftIndex]:
                temp = rootNode.custom_list[index]
                rootNode.custom_list[index] = rootNode.custom_list[leftIndex]
                rootNode.custom_list[leftIndex] = temp
            return
    else:
        if heapType == "Min":
            if rootNode.custom_list[leftIndex] < rootNode.custom_list[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.custom_list[index] > rootNode.custom_list[swapChild]:
                temp = rootNode.custom_list[index]
                rootNode.custom_list[index] = rootNode.custom_list[swapChild]
                rootNode.custom_list[swapChild] = temp
        else:
            if rootNode.custom_list[leftIndex] > rootNode.custom_list[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.custom_list[index] < rootNode.custom_list[swapChild]:
                temp = rootNode.custom_list[index]
                rootNode.custom_list[index] = rootNode.custom_list[swapChild]
                rootNode.custom_list[swapChild] = temp

        heapifyTreeExtract(rootNode, swapChild, heapType)


def extractNode(rootNode, heapType):
    if rootNode.heap_size == 0:
        return
    else:
        extractedNode = rootNode.custom_list[1]
        rootNode.custom_list[1] = rootNode.custom_list[rootNode.heap_size]
        rootNode.custom_list[rootNode.heap_size] = None
        rootNode.heap_size -= 1
        heapifyTreeExtract(rootNode, 1, heapType)
        return extractedNode


def deleteEntireBP(rootNode):
    rootNode.customList = None

