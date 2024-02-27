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
        popped_node = self.tail
        if not self.head:
            return None
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        popped_node.prev = None
        self.length -= 1
        return popped_node

    def remove(self, index):
        """
        Removes and returns the node at the specified index in the doubly linked list.

        Parameters:
        - index: The index of the node to be removed.

        Returns:
        - The removed node, or None if the index is out of bounds.

        Explanation:
        - Check if the index is out of bounds; if so, return None.
        - If the index is 0, remove and return the first node using pop_first().
        - If the index is equal to the last index, remove and return the last node using pop().
        - Otherwise, get the node at the specified index, update the links of the surrounding nodes,
          and return the removed node.
        """
        # Check if the index is out of bounds; if so, return None
        if index < 0 or index >= self.length:
            return None

        # If the index is 0, remove and return the first node using pop_first()
        if index == 0:
            return self.pop_first()

        # If the index is equal to the last index, remove and return the last node using pop()
        if index == self.length - 1:
            return self.pop()

        # Get the node at the specified index
        popped_node = self.get(index)

        # Update the links of the surrounding nodes
        popped_node.prev.next = popped_node.next
        popped_node.next.prev = popped_node.prev

        # Set the next and previous references of the removed node to None
        popped_node.next = None
        popped_node.prev = None

        # Decrement the length of the doubly linked list
        self.length -= 1

        # Return the removed node
        return popped_node



