class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CSLinkedList: # you can use this as well
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
                result += '-->'
            temp_node = temp_node.next
        return result

    def append(self, value):
        # Create a new node with the given value
        new_node = Node(value)

        # Check if the linked li st is empty
        if self.length == 0:
            # If empty, set both head and tail to the new node
            self.head = new_node
            self.tail = new_node
            # Make the new node point to itself since it's the only node in the list
            new_node.next = new_node
        else:
            # If not empty, update the next pointer of the current tail to the new node
            self.tail.next = new_node
            # Make the new node point to the head since it's the new tail in a circular list
            new_node.next = self.head
            # Update the tail to the newly added node
            self.tail = new_node

        # Increment the length of the linked list
        self.length += 1


cslinkedlist = CSLinkedList()
print(cslinkedlist.append(10))
print(cslinkedlist.append(20))
print(cslinkedlist)

