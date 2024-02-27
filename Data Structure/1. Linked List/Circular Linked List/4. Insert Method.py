class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class CSLinkedList:
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
            if temp_node == self.head:
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
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        self.length += 1

    def insert(self, index, value):
        # Create a new node with the given value
        new_node = Node(value)

        # Insert at the beginning of the linked list
        if index == 0:
            # If the list is empty, set both head and tail to the new node
            if self.length == 0:
                self.head = new_node
                self.tail = new_node
            else:
                # If not empty, update pointers for insertion at the beginning
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node  # Update tail's next to maintain circularity

        # Insert at the end of the linked list
        elif index == self.length:
            # Update tail's next to point to the new node
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node  # Update tail to the new node to maintain circularity

        # Insert at any other index
        else:
            # Traverse the list to the node at index - 1
            current_node = self.head
            for _ in range(index - 1):
                current_node = current_node.next

            # Update pointers for insertion at the specified index
            new_node.next = current_node.next
            current_node.next = new_node

        # Increment the length of the linked list
        self.length += 1






cslinkedlist = CSLinkedList()
cslinkedlist.append(20)
cslinkedlist.append(30)
cslinkedlist.append(40)
cslinkedlist.insert(1,99)
print(cslinkedlist.traversal())
print(cslinkedlist.search(99))
