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
        new_node = Node(value)
        if index == 0:
            if self.length == 0:
                self.head = new_node
                self.tail = new_node
            else:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
        elif index == self.length:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        else:
            current_node = self.head
            for _ in range(index - 1):
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node
        self.length += 1

    def traversal(self):
        current_node = self.head
        while current_node is not None:
            print(current_node)
            current_node = current_node.next
            if current_node == self.head:
                break

    def search(self, value):
        # Start from the head of the linked list
        current_node = self.head

        # Initialize index for tracking the position of the current node
        index = 0

        # Traverse the circular list
        while current_node is not None:
            # Check if the value of the current node matches the target value
            if current_node.value == value:
                # Return True if a match is found
                return index

            # Move to the next node
            current_node = current_node.next

            # Check if we have completed one full traversal of the circular list
            if current_node == self.head:
                break

            # Increment the index for tracking the position
            index += 1

        # Return False if the value is not found in the list
        return False

cslinkedlist = CSLinkedList()
cslinkedlist.append(20)
cslinkedlist.append(30)
cslinkedlist.append(40)
cslinkedlist.insert(1, 99)
print(cslinkedlist.traversal())
print(cslinkedlist.search(99))
