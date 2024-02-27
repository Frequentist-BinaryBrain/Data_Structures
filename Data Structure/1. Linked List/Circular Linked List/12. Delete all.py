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
        current_node = self.head
        index = 0
        while current_node is not None:
            if current_node.value == value:
                return index
            current_node = current_node.next
            if current_node == self.head:
                break
            index += 1
        return False

    def get(self, index):
        if index == -1:
            return self.tail
        elif index < -1 or index >= self.length:
            return None

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        return current_node

    def set(self, index, value):
        temp = self.get(index)
        while temp:
            temp.value = value
            return True
        return False

    def pop_first(self):
        if self.length == 0:
            return None

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            popped_node = self.head
            self.head = self.head.next
            self.tail.next = self.head
            popped_node.next = None
        self.length -= 1
        return popped_node

    def pop(self, index):
        popped_node = self.tail

        if self.length == 1:
            self.head = self.tail = None

        temp = self.head

        while temp.next is not self.tail:
            temp = temp.next

        temp.next = self.head
        self.tail = temp
        popped_node.next = None
        self.length -= 1
        return popped_node

    def remove(self, index):

        if index == 0:
            return self.pop_first()

        elif index >= self.length or index < 0:
            return None
        elif index == self.length -1:
            return self.pop()

        prev_node = self.get(index-1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length -= 1
        return popped_node

    def delete(self):
        if self.length == 0:
            return None
        self.tail.next = None
        self.head = None
        self.tail  = None
        self.length = 0








