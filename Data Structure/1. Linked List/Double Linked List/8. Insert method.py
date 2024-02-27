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
        if index < 0 or index >= self.length:
            return None

        if index < self.length // 2:
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
        else:
            current_node = self.tail
            for _ in range(self.length - 1, index, -1):
                current_node = current_node.prev

        return current_node

    def set(self, index, value):
        node = self.get(index=index)
        if node is not None:
            node.value = value
            return True
        return False


    def insert(self, index, value):
        """
        Inserts a new node with the given value at the specified index in the doubly linked list.

        Parameters:
        - index: The index at which to insert the new node.
        - value: The value to be added to the new node.

        Returns:
        - True if the insertion is successful, False if the index is out of bounds.

        Explanation:
        - If the index is less than 0 or greater than the length of the list, return False.
        - If the index is 0, prepend the value to the list.
        - If the index is equal to the length of the list, append the value to the list.
        - Otherwise, find the node at the previous index, and insert the new node after it.
        - Update the links to properly link the new node into the list.
        - Increment the length of the doubly linked list.
        """
        # Create a new node with the given value
        new_node = Node(value)

        # Check if the index is out of bounds
        if index < 0 or index > self.length:
            return False
        # If the index is 0, prepend the value to the list
        elif index == 0:
            self.prepend(value)
            return True
        # If the index is equal to the length, append the value to the list
        elif index == self.length:
            self.append(value)
            return True

        # Find the node at the previous index
        temp_node = self.get(index - 1)

        # Insert the new node after the previous node
        new_node.next = temp_node.next
        new_node.prev = temp_node
        temp_node.next.prev = new_node
        temp_node.next = new_node

        # Increment the length of the doubly linked list
        self.length += 1
        return True



