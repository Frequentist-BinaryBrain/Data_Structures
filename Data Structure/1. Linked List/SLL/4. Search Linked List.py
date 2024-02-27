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
        new_node = Node(value)
        if index < 0 or index > self.length:
            return False
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            for _ in range(index - 1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1
        return True

    def traversal(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next


    def search(self, target):
        # Start from the head of the linked list
        current = self.head      # O(1)
        index = 0                 # O(1)
        # Traverse the linked list
        while current is not None:   # O(N)
            # Check if the value of the current node matches the target value
            if current.value == target:  # O(1)
                # If a match is found, return True
                return index            # O(1)
            else:
                # Move to the next node in the linked list
                current = current.next      # O(1)
                index += 1              # O(1)

        # If the loop completes without finding a match
        return -1


new_linked_list = LinkedList()
new_linked_list.append(10)
print(new_linked_list.length)
print(new_linked_list)
new_linked_list.prepend(55)
print(new_linked_list)
new_linked_list.insert(1, 50)
print(new_linked_list)
print(new_linked_list.search(10))

