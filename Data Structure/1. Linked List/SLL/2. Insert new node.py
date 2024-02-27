class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += '-->'
            temp_node = temp_node.next
        return result

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1

    def insert(self, index, value):
        # Create a new node with the given value
        new_node = Node(value)

        # Check if the index is out of bounds
        if index < 0 or index > self.length:
            return False

        # Handle the case where the linked list is empty
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        # Handle the case where the new node is inserted at the beginning
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            # Start from the head of the linked list
            temp_node = self.head

            # Traverse to the node at index - 1
            for _ in range(index - 1):
                temp_node = temp_node.next

            # Insert the new node at the specified index
            new_node.next = temp_node.next
            temp_node.next = new_node

        # Increment the length of the linked list
        self.length += 1

        # Return True to indicate successful insertion
        return True

# Here, the loop runs index - 1 times, and the loop variable _ is not used within the loop body.
# It's a way to indicate that the loop is being used for its side effects (in this case, traversing the linked list) and
# not for the value of the loop variable.






new_linked_list = LinkedList()
new_linked_list.append(10)
print(new_linked_list.length)
print(new_linked_list)
new_linked_list.prepend(55)
print(new_linked_list)
new_linked_list.insert(1, 50)
print(new_linked_list)
new_linked_list.insert(-1, 50)
print(new_linked_list)


