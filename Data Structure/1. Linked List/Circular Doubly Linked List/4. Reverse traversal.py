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

    def insertCDLL(self, value, location):
        if self.head is None:
            return "The CDLL doesn't exist"
        else:
            newNode = Node(value)

            if location == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode

            elif location == 1:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.tail.next = newNode
                self.tail = newNode

            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1

                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode

            return "The node has been successfully inserted"

    def traversal(self):
        if self.head is None:
            print("There is not any node for traversal")
        else:
            current_node = self.head
            while True:
                print(current_node.value)
                if current_node == self.tail:
                    break
                current_node = current_node.next

    def reverse_traversal(self):
        if self.head is None:
            print("There is not any node for reversal")
        else:
            # Start traversal from the tail
            current_node = self.tail

            # Loop through the list in reverse order
            while current_node is not self.head:
                print(current_node.value)

                # Move to the previous node
                current_node = current_node.prev

            # Print the value of the head (last node in the circular list)
            print(current_node.value)



circularDLL = CircularDoublyLinkedList()
print(circularDLL.createCDLL(5))
circularDLL.insertCDLL(0, 0)
circularDLL.insertCDLL(1, 1)
circularDLL.insertCDLL(2, 2)
print(circularDLL)
print([node.value for node in circularDLL])
print(circularDLL.reverse_traversal())
