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
        """
        Appends a new node with the given value to the end of the doubly linked list.

        Parameters:
        - value: The value to be added to the new node.

        Explanation:
        - Create a new node with the given value.
        - If the list is empty, set both head and tail to the new node.
        - Otherwise, update the tail's next reference and the new node's previous reference.
        - Set the tail to the new node.
        - Increment the length of the doubly linked list.
        """
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

        Explanation:
        - Create a new node with the given value.
        - If the list is empty, set both head and tail to the new node.
        - Otherwise, update the head's previous reference and the new node's next reference.
        - Set the head to the new node.
        - Increment the length of the doubly linked list.
        """
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
        """
        Traverses the doubly linked list from the head to the tail, printing each node's value.
        """
        current_node = self.head
        while current_node:
            print(current_node)
            current_node = current_node.next

    def reverse_traversal(self):
        """
        Traverses the doubly linked list from the tail to the head, printing each node's value.
        """
        current_node = self.tail

        while current_node:
            print(current_node.value)
            current_node = current_node.prev

    def search(self, target):
        """
        Searches for a node with the given value in the doubly linked list.

        Parameters:
        - target: The value to search for.

        Returns:
        - The index of the first occurrence of the value, or -1 if not found.
        """
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

    def set(self, index, value):
        """
        Sets the value of the node at the specified index in the doubly linked list.

        Parameters:
        - index: The index of the node to set the value for.
        - value: The new value to assign to the node.

        Returns:
        - True if the operation is successful, False if the index is out of bounds.
        """
        # Get the node at the specified index
        node = self.get(index=index)

        # If the node exists, set its value and return True
        if node is not None:
            node.value = value
            return True

        # If the index is out of bounds, return False
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
        - Create a new node with the given value.
        - Check if the index is out of bounds; if so, return False.
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

    def pop_first(self):
        """
        Removes and returns the first node from the doubly linked list.

        Returns:
        - The node that was removed, or None if the list is empty.

        Explanation:
        - Save a reference to the current head as the node to be popped.
        - If the list has only one node, set both head and tail to None.
        - If the list has more than one node, update the head to the next node and
          adjust the new head's previous reference to None.
        - Set the popped node's next reference to None.
        - Decrement the length of the doubly linked list.
        """
        # Save a reference to the current head as the node to be popped
        popped_node = self.head

        # Check if the list has only one node
        if self.length == 1:
            self.head = self.tail = None
        else:
            # If the list has more than one node, update the head to the next node
            # and adjust the new head's previous reference to None
            self.head = self.head.next
            self.head.prev = None

        # Set the popped node's next reference to None
        popped_node.next = None

        # Decrement the length of the doubly linked list
        self.length -= 1

        # Return the popped node
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
