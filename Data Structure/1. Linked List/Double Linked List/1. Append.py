class Node:
    def __init__(self, value):
        """
        Constructor for the Node class.

        Parameters:
        - value: The value to be stored in the node.
        """
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return f'{self.value}'

class DoubleLinkedList:
    def __init__(self):
        """
        Constructor for the LinkedList class.
        Initializes an empty linked list with no nodes.
        """
        self.head = None
        self.tail = None
        self.length = 0  # Initial length of the linked list is set to zero.

    def __str__(self):
        """
        Returns a string representation of the doubly linked list.

        Returns:
        - result: String representation of the doubly linked list.
        """
        temp_node = self.head
        result = ''

        while temp_node is not None:
            result += str(temp_node.value)

            if temp_node.next is not None:
                # If there is a next node, append '<-->' to separate values in the representation.
                result += '<-->'

            temp_node = temp_node.next

        return result


    def append(self, value):
        """
        Appends a new node with the given value to the end of the doubly linked list.

        Parameters:
        - value: The value to be added to the new node.
        """
        new_node = Node(value)

        if self.length == 0:
            # If the list is empty, the new node becomes both the head and the tail.
            self.head = new_node
            self.tail = new_node
        else:
            # If the list is not empty, update the tail's next to the new node,
            # set the new node's previous to the current tail, and update the tail to the new node.
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        # Increment the length of the doubly linked list.
        self.length += 1

newDLL = DoubleLinkedList()
newDLL.append(20)
newDLL.append(30)
print(newDLL)
