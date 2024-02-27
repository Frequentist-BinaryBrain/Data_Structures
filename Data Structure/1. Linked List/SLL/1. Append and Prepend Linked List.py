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
        # Create a new node with the given value
        new_node = Node(value)   # O(1)
        # Check if the linked list is empty
        if self.head is None:    # O(1)
            # If the list is empty, set both head and tail to the new node
            self.head = new_node   # O(1)
            self.tail = new_node   # O(1)
            self.length += 1
        else:
        # If the list is not empty, insert the new node at the beginning (before the current head)
            new_node.next = self.head    # O(1)
            self.head = new_node        # O(1)
            self.length += 1

new_linked_list = LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(40)
new_linked_list.append(60)
new_linked_list.append(90)
print(new_linked_list.length)
print(new_linked_list)
new_linked_list.prepend(55)
print(new_linked_list)

