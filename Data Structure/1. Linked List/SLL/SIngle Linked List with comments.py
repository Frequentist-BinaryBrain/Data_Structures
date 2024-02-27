class Node:
    def __init__(self, value):
        # Node class constructor to initialize a new node with a given value
        self.value = value
        self.next = None  # Pointer to the next node in the linked list

class LinkedList:

    def __init__(self):
        # LinkedList class constructor to initialize an empty linked list
        self.head = None  # Head pointer to the first node
        self.tail = None  # Tail pointer to the last node
        self.length = 0   # Variable to track the number of nodes in the linked list

    def append(self, value):
        # Method to add a new node with the given value to the end of the linked list
        new_node = Node(value)

        # Check if the linked list is empty
        if self.head is None:
            # If empty, set both head and tail to the new node
            self.head = new_node
            self.tail = new_node
        else:
            # If not empty, add the new node to the end of the linked list
            self.tail.next = new_node
            self.tail = new_node

        # Increase the length of the linked list by 1
        self.length += 1

    def __str__(self):
        # Method to create a string representation of the linked list
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += '-->'
            temp_node = temp_node.next
        return result

    def prepend(self, value):
        # Method to add a new node with the given value to the beginning of the linked list
        new_node = Node(value)

        # Check if the linked list is empty
        if self.head is None:
            # If empty, set both head and tail to the new node
            self.head = new_node
            self.tail = new_node
        else:
            # If not empty, add the new node to the beginning of the linked list
            new_node.next = self.head
            self.head = new_node

        # Increase the length of the linked list by 1
        self.length += 1

    def insert(self, index, value):
        # Method to insert a new node with the given value at the specified index
        new_node = Node(value)

        # Check if the index is out of bounds
        if index < 0 or index > self.length:
            return False

        # Check if the linked list is empty
        if self.length == 0:
            # If empty, set both head and tail to the new node
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            # If the index is 0, add the new node to the beginning of the linked list
            new_node.next = self.head
            self.head = new_node
        else:
            # Traverse the linked list to the specified index
            temp_node = self.head
            for _ in range(index - 1):
                temp_node = temp_node.next

            # Insert the new node at the specified index
            new_node.next = temp_node.next
            temp_node.next = new_node

        # Increase the length of the linked list by 1
        self.length += 1
        return True

    def traversal(self):
        # Method to traverse the linked list and print each node's value
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

    def search(self, target):
        # Method to search for a target value in the linked list and return its index
        current = self.head
        index = 0
        while current is not None:
            if current.value == target:
                return index
            else:
                current = current.next
                index += 1
        return -1

    def get(self, index):
        # Method to get the node at the specified index
        if index == -1:
            return self.tail
        if index < -1 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def set_value(self, index, value):
        # Method to set the value of the node at the specified index
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False

    def pop_first(self):
        # Method to pop the node at the beginning of the linked list
        if self.length == 0:
            return None

        popped_node = self.head

        if self.length == 1:
            # If there is only one node, update both head and tail to None
            self.head = None
            self.tail = None
        else:
            # Update the head to be the next node in the list
            self.head = self.head.next
            popped_node.next = None

        # Decrease the length of the linked list by 1
        self.length -= 1

        return popped_node

    def pop(self):
        # Method to pop the node at the end of the linked list
        if self.length == 0:
            return None

        popped_node = self.tail

        if self.length == 1:
            # If there is only one node, update both head and tail to None
            self.head = None
            self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next

            # Update the tail to be the found node, disconnecting the current tail
            self.tail = temp
            temp.next = None

        # Decrease the length of the linked list by 1
        self.length -= 1

        return popped_node

    def remove(self, index):
        # Method to remove the node at the specified index
        if index >= self.length or index < -1:
            return None

        # Check if the node at the beginning should be removed
        if index == 0:
            return self.pop_first()

        # Check if the node at the end should be removed
        if index == self.length - 1 or index == -1:
            return self.pop()

        # Find the node before the one to be removed (previous node)
        prev_node = self.get(index - 1)

        # Get the node to be removed (the one after the previous node)
        popped_node = prev_node.next

        # Update the previous node's next pointer to skip the popped node
        prev_node.next = popped_node.next

        # Disconnect the popped node from the rest of the linked list
        popped_node.next = None

        # Decrease the length of the linked list by 1
        self.length -= 1

        # Return the popped node
        return popped_node

    def delete_all(self):
        # Method to delete all nodes in the linked list
        # Set both head and tail to None, effectively clearing the linked list
        self.head = None
        self.tail = None

        # Reset the length to 0
        self.length = 0
