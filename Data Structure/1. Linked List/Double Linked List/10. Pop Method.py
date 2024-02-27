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
        new_node = Node(value)
        if index < 0 or index > self.length:
            return False
        if index == 0:
            self.prepend(value)
            return True
        elif index == self.length:
            self.append(value)
            return True
        temp_node = get(index - 1)
        new_node.next = temp_node.next
        new_node.prev = temp_node
        temp_node.next.prev = new_node
        temp_node.next = new_node
        self.length += 1
        return True

    def pop_first(self):
        popped_node = self.head
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        popped_node.next = None
        self.length -= 1
        return popped_node

    def pop(self):
        """
        Removes and returns the last node from the doubly linked list.

        Returns:
        - The node that was removed, or None if the list is empty.

        Explanation:
        - Save a reference to the current tail as the node to be popped.
        - Check if the list is empty; if so, return None.
        - If the list has only one node, set both head and tail to None.
        - If the list has more than one node, update the tail to the previous node and
          adjust the new tail's next reference to None.
        - Set the popped node's previous reference to None.
        - Decrement the length of the doubly linked list.
        """
        # Save a reference to the current tail as the node to be popped
        popped_node = self.tail

        # Check if the list is empty; if so, return None
        if not self.head:
            return None

        # If the list has only one node, set both head and tail to None
        if self.length == 1:
            self.head = self.tail = None
        else:
            # If the list has more than one node, update the tail to the previous node
            # and adjust the new tail's next reference to None
            self.tail = self.tail.prev
            self.tail.next = None

        # Set the popped node's previous reference to None
        popped_node.prev = None

        # Decrement the length of the doubly linked list
        self.length -= 1

        # Return the popped node
        return popped_node







current = DoubleLinkedList()
current.append(23)
current.append(13)
current.append(27)
print(current)
current.pop_first()
print(current)
