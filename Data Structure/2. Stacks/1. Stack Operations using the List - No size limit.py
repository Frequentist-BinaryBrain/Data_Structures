class Stack:
    def __init__(self):
        # Initialize an empty list to represent the stack
        self.list = []

    def __str__(self):
        # Create a reversed copy of the list for display purposes
        reversed_copy = self.list[::-1]

        # Convert each element in the list to a string
        values = [str(x) for x in reversed_copy]

        # Join the string representations of elements with a newline character
        return '\n'.join(values)

    def isEmpty(self):

        if self.list == []:
            return True
        else:
            return False

    def push(self, value):
        self.list.append(value)
        # Return the modified stack for potential further use
        return self.list

    # Pop
    def pop(self):
        if self.isEmpty():
            return "No element in the Stack"
        else:
            # Pop and return the top element from the stack
            return self.list.pop()

    def peek(self):
            if self.isEmpty():
                # If the stack is empty, return a message
                return "No element in the Stack"
            else:
                # Return the top element from the stack without popping
                return self.list[-1]

    def delete(self):
        self.list = None


# Example usage:
my_stack = Stack()

# Pushing elements onto the stack and printing the updated stack
print("Pushing 12", my_stack.push(12))
print("Pushing 22", my_stack.push(22))
print("Pushing 25", my_stack.push(25))
print(my_stack)

# Popping an element from the stack and printing the updated stack
popped_element = my_stack.pop()
print("Popped Element:", popped_element)
print(my_stack)
print("top element is:", my_stack.peek())
print("Deleted the stack :", my_stack.delete())




