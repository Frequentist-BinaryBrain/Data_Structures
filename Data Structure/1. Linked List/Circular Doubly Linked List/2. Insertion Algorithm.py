class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    def createCDLL(self, nodeValue):
        newNode = Node(nodeValue)
        self.head = newNode
        self.tail = newNode
        newNode.prev = newNode
        newNode.next = newNode
        return 'The CDLL is created successfully'

       # Insertion Method in Circular Doubly Linked List
    def insertCDLL(self, value, location):
        # Check if the CDLL is empty
        if self.head is None:
            return "The CDLL doesn't exist"
        else:
            # Create a new node with the given value
            newNode = Node(value)

            # Insert at the beginning
            if location == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode   # Update the previous pointer of the current head to newNode
                self.head = newNode   # Update the head to newNode
                self.tail.next = newNode   # Update the next pointer of the current tail to newNode

            # Insert at the end
            elif location == 1:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode   # Update the previous pointer of the current head to newNode
                self.tail.next = newNode   # Update the next pointer of the current tail to newNode
                self.tail = newNode   # Update the tail to newNode

            # Insert at a specified location
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1

                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode   # Update the previous pointer of the next node to newNode
                tempNode.next = newNode   # Update the next pointer of the current node to newNode

            return "The node has been successfully inserted"

#      When location == 0, the code inserts the new node at the beginning of the list.
#      When location == 1, the code inserts the new node at the end of the list.
#      For other values of location (greater than 1), the code inserts the new node at the specified location in the list.

circularDLL = CircularDoublyLinkedList()
print(circularDLL.createCDLL(5))
circularDLL.insertCDLL(0, 0)
circularDLL.insertCDLL(1, 1)
circularDLL.insertCDLL(2, 2)
print(circularDLL)
print([node.value for node in circularDLL])
