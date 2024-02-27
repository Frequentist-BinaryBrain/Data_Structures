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
            current_node = self.tail
            while current_node is not self.head:
                print(current_node.value)
                current_node = current_node.prev
            print(current_node.value)

    def search(self, target):
        if self.head is None:
            return 'There is not any node in CDLL'
        else:
            current_node = self.head
            index = 0

            while current_node is not self.tail:
                if current_node.value == target:
                    return index
                else:
                    current_node = current_node.next
                    index += 1

            if current_node.value == target:
                return index

            return "Value doesn't exist in our CDLL"

    def delete_node(self, location):
        if self.head is None:
            return "There is not any node to delete"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    current_node = self.head
                    index = 0
                    while index < location - 1:
                        current_node = current_node.next
                        index += 1
                    current_node.next = current_node.next.next
                    current_node.next.prev = current_node

        return "The node has been successfully deleted"

    def delete_all_nodes(self):
        # Check if the list is empty
        if self.head is None:
            return "There is not any element to delete"

        else:
            # Disconnect the tail's next pointer to break the circular structure
            self.tail.next = None

            # Traverse the list and remove the previous pointers to disconnect each node
            current_node = self.head
            while current_node:
                current_node.prev = None
                current_node = current_node.next
    
            # Reset head and tail to None for an empty list
            self.head = None
            self.tail = None
            print("The CDLL has been deleted successfully")





# Example usage
circularDLL = CircularDoublyLinkedList()
print(circularDLL.createCDLL(5))
circularDLL.insertCDLL(0, 0)
circularDLL.insertCDLL(1, 1)
circularDLL.insertCDLL(2, 2)
print(circularDLL)
print([node.value for node in circularDLL])
print(circularDLL.delete_node(1))
print([node.value for node in circularDLL])
