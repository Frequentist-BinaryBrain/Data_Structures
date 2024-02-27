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
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            new_node.prev = None

        self.length += 1

    def traversal(self):
        current_node = self.head
        while current_node:
            print(current_node)
            current_node = current_node.next

    def reverse_traversal(self):
        current_node = self.tail

        while current_node:
            print(current_node.value)
            current_node = current_node.prev

    def search(self, target):
        current_node = self.head
        index = 0

        while current_node:
            if current_node.value == target:
                return index
            else:
                current_node = current_node.next
                index += 1

        return -1

    def get(self, index):

        if index < self.length //2:
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
        else:
            current_node = self.tail
            for _ in range(self.length -1, index, -1):
                current_node = current_node.prev



    def get(self, index):
        """
        Gets the node at the specified index in the doubly linked list.

        Parameters:
        - index: The index of the node to retrieve.

        Returns:
        - The node at the specified index, or None if the index is out of bounds.

        Explanation:
        - To optimize traversal, the method checks whether the desired index is closer to the
          head or tail of the doubly linked list.
        - If the index is in the first half, it starts traversal from the head.
        - If the index is in the second half, it starts traversal from the tail.
        """
        # Check for invalid index values
        if index < 0 or index >= self.length:
            return None

        # Optimize traversal based on index location
        if index < self.length // 2:
            # If the index is in the first half, start traversal from the head
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
        else:
            # If the index is in the second half, start traversal from the tail
            current_node = self.tail
            for _ in range(self.length - 1, index, -1):
                current_node = current_node.prev

        return current_node











