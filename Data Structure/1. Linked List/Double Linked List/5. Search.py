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
        """
        Searches for a given target value in the doubly linked list.

        Parameters:
        - target: The value to search for.

        Returns:
        - The index of the first occurrence of the target value, or -1 if not found.
        """
        current_node = self.head
        index = 0

        while current_node:
            if current_node.value == target:
                # If the current node's value matches the target, return the current index
                return index
            else:
                # Move to the next node and increment the index
                current_node = current_node.next
                index += 1

        # If the target value is not found in the list, return -1
        return -1



