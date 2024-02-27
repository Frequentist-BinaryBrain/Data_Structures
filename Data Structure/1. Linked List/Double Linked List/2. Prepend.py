class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return f'{self.value}'

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ''

        while temp_node is not None:
            result += str(temp_node.value)

            if temp_node.next is not None:
                result += '<-->'

            temp_node = temp_node.next

        return result

    def append(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.length += 1


    def prepend(self, value):
        """
        Prepends a new node with the given value to the beginning of the doubly linked list.

        Parameters:
        - value: The value to be added to the new node.
        """
        new_node = Node(value)

        if self.length == 0:
            # If the list is empty, the new node becomes both the head and the tail.
            self.head = new_node
            self.tail = new_node
        else:
            # If the list is not empty, update the new node's next to the current head,
            # set the current head's previous to the new node, and update the head to the new node.
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            new_node.prev = None

        # Increment the length of the doubly linked list.
        self.length += 1




newDLL = DoubleLinkedList()
newDLL.append(20)
newDLL.append(30)
print(newDLL)
