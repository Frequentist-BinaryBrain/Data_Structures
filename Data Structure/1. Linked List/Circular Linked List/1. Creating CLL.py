class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CSLinkedList:
    def __init__(self, value):
        # Create a new node with the given value
        new_node = Node(value)

        # Since this is a circular singly linked list,
        # the next pointer of the new node is set to itself
        new_node.next = new_node  # Because the last node will be referenced to the first node

        # Set the head and tail of the linked list to the new node
        self.head = new_node
        self.tail = new_node

        # Initialize the length of the linked list to 1
        self.length = 1





cslinkedlist = CSLinkedList(10)
print(cslinkedlist.head.value)
