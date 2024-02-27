# Definition of the Node class representing a node in the circular doubly linked list
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

# Definition of the CircularDoublyLinkedList class
class CircularDoublyLinkedList:
    def __init__(self):
        # Initialization of head and tail to None when the list is created
        self.head = None
        self.tail = None

    # Iterator method to traverse the circular doubly linked list
    def __iter__(self):
        node = self.head
        # Iterate through nodes until tail is reached in the circular list
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    # Method to create a circular doubly linked list with a single node
    def createCDLL(self, nodeValue):
        # Create a new node with the given value
        newNode = Node(nodeValue)
        # Set the head and tail to the new node, making it a circular list with one element
        self.head = newNode
        self.tail = newNode
        newNode.prev = newNode
        newNode.next = newNode
        return 'The CDLL is created successfully'

    # Method to insert a node into the circular doubly linked list at a specified location
    def insertCDLL(self, value, location):
        # Check if the CDLL is empty
        if self.head is None:
            return "The CDLL doesn't exist"
        else:
            # Create a new node with the given value
            newNode = Node(value)

            # Insert at the beginning of the list
            if location == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode

            # Insert at the end of the list
            elif location == 1:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.tail.next = newNode
                self.tail = newNode

            # Insert at a specified location
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

    # Method to traverse the circular doubly linked list and print node values
    def traversal(self):
        # Check if the list is empty
        if self.head is None:
            print("There is not any node for traversal")
        else:
            # Start traversal from the head
            current_node = self.head
            while True:
                print(current_node.value)
                if current_node == self.tail:
                    break
                current_node = current_node.next

    # Method to traverse the circular doubly linked list in reverse order and print node values
    def reverse_traversal(self):
        # Check if the list is empty
        if self.head is None:
            print("There is not any node for reversal")
        else:
            # Start traversal from the tail
            current_node = self.tail
            # Loop through the list in reverse order
            while current_node is not self.head:
                print(current_node.value)
                current_node = current_node.prev
            # Print the value of the head (last node in the circular list)
            print(current_node.value)

    # Method to search for a target value in the circular doubly linked list
    def search(self, target):
        # Check if the list is empty
        if self.head is None:
            return 'There is not any node in CDLL'
        else:
            current_node = self.head  # Start searching from the head
            index = 0

            # Iterate through the circular list until the tail is reached
            while current_node is not self.tail:
                if current_node.value == target:
                    return index  # Return the index if the target is found
                else:
                    current_node = current_node.next
                    index += 1

            # Check the last node (tail) after the loop
            if current_node.value == target:
                return index  # Return the index if the target is found in the last node

            # Return a message if the target is not found in the circular list
            return "Value doesn't exist in our CDLL"

    # Method to delete a node at a specified location in the circular doubly linked list
    def delete_node(self, location):
        # Check if the list is empty
        if self.head is None:
            return "There is not any node to delete"  # Return message for an empty list
        else:
            # Delete the node at the specified location
            if location == 0:
                # Check if there is only one node in the list
                if self.head == self.tail:
                    # Reset head and tail to None for an empty list
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    # Move head to the next node and update pointers
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == 1:
                # Check if there is only one node in the list
                if self.head == self.tail:
                    # Reset head and tail to None for an empty list
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    # Traverse to the node at the specified location and update pointers
                    current_node = self.head
                    index = 0
                    while index < location - 1:
                        current_node = current_node.next
                        index += 1
                    current_node.next = current_node.next.next
                    current_node.next.prev = current_node

        return "The node has been successfully deleted"  # Return success message

    # Method to delete all nodes in the circular doubly linked list
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
