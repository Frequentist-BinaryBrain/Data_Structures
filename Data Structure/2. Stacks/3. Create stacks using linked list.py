class Node:
    def __init__(self, value=None):
        # Initialize a node with a given value and a reference to the next node (default is None)
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        # Initialize an empty linked list with no head
        self.head = None

    def __iter__(self):
        # Initialize the current node to the head of the linked list
        current_node = self.head

        # Iterate through the linked list using a while loop
        while current_node:
            # Yield the current node, allowing it to be accessed in the loop
            yield current_node

            # Move to the next node in the linked list
            current_node = current_node.next

            # The loop continues until current_node becomes None, indicating the end of the list

# The LinkedList class represents a linked list where each element is a Node containing a value and a reference to the next Node.
# The __iter__ method allows iterating over the elements of the linked list using a while loop and the yield keyword.

class Stack:
    def __init__(self):
        # Initialize a stack using a linked list
        self.LinkedList = LinkedList()

    def __str__(self):
        # Convert the stack to a string representation
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values)

    def isEmpty(self):
        # Check if the stack is empty
        return self.LinkedList.head is None

    # Important Note:
    # If you were to use self.head directly in the Stack class without referencing the LinkedList instance,
    # Python would look for a head attribute directly within the Stack class, and it would not find it. This would result in an AttributeError

#   In the pop method of the Stack class, the head of the linked list is "popped out" because it follows the Last In, First Out (LIFO) principle of a stack.
#   When you push elements onto the stack using the push method, each new element becomes the new head of the linked list, and it points to the previous head.

    def push(self, value):
        # Push a new node with the given value onto the stack
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node

    def pop(self):
        # Pop the top element from the stack
        if self.isEmpty():
            return "There is no element in the stack"
        else:
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodeValue

    def peek(self):
        # Peek at the top element of the stack without removing it
        if self.isEmpty():
            return "There is no element in the stack"
        else:
            nodeValue = self.LinkedList.head.value
            return nodeValue

# Example usage:
custom_stack = Stack()
custom_stack.push(1)
custom_stack.push(2)
custom_stack.push(3)
custom_stack.push(4)
print(custom_stack)
print("------------")
custom_stack.pop()
print(custom_stack)
print("------------")
print(custom_stack.peek())


#Use Stacks:

#    LIFO Functionality:
#        Stacks are optimal when you need to maintain a Last In, First Out (LIFO) order for elements.
#        This is beneficial in scenarios like function call management, undo mechanisms, and backtracking.

#    Minimizing Data Corruption:
#        Due to the LIFO nature, stacks are often used to ensure that the most recently added data is the first to be processed.
#        This can help minimize data corruption in certain scenarios.

#Avoid Stacks:

#    Random Access Limitations:
#        Stacks are not suitable for scenarios where you require frequent random access to elements.
#        Retrieving elements in the middle or at the end of a stack involves popping elements in a sequential manner, making it inefficient.

