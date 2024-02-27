class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class CSLinkedList:
    # def __init__(self, value):
    #     new_node = Node(value)
    #     new_node.next = new_node
    #     self.head = new_node
    #     self.tail = new_node
    #     self.length = 1

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:  # Stop condition for circular list
                break
            result += ' -> '
        return result

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        # Create a new node with the given value
        new_node = Node(value)

        # If the linked list is empty, set both head and tail to the new node
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            # Make the new node point to itself since it's the only node in the list
            new_node.next = new_node
        else:
            # If not empty, set the next pointer of the new node to the current head
            new_node.next = self.head
            # Update the head to the new node
            self.head = new_node
            # Make the tail point to the new head to maintain circularity
            self.tail.next = new_node

        # Increment the length of the linked list
        self.length += 1

cslinkedlist = CSLinkedList()
cslinkedlist.append(20)
cslinkedlist.append(30)
cslinkedlist.append(40)
cslinkedlist.prepend(20)
print(cslinkedlist)
