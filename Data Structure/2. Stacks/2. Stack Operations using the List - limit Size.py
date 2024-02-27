class Stacks:
    def __init__(self, maxsize):
        # Initialize the stack with a maximum size
        self.maxsize = maxsize
        # Initialize an empty list to represent the stack
        self.list = []

    def __str__(self):
        # Create a reversed copy of the list for display purposes
        reversed_copy = self.list[::-1]

        # Convert each element in the list to a string
        values = [str(x) for x in reversed_copy]

        # Join the string representations of elements with a newline character
        return '\n'.join(values)

    # isEmpty
    def isempty(self):
        # Check if the list (stack) is empty
        return not bool(self.list)

    # isFull
    def isfull(self):
        # Check if the list (stack) is full based on the maximum size
        return len(self.list) == self.maxsize

    # Push
    def push(self, value):
        # Check if the stack is full before pushing
        if self.isfull():
            return "The stack is full"
        else:
            # Add the value to the stack
            self.list.append(value)
            # Print a success message
            print(f"The {value} is successfully added to the list")

    # Pop
    def pop(self):
        # Check if the stack is empty before popping
        if self.isempty():
            return "No element in the Stack"
        else:
            # Pop and return the top element from the stack
            return self.list.pop()

    # Peek
    def peek(self):
        # Check if the stack is empty before peeking
        if self.isempty():
            # If the stack is empty, return a message
            return "No element in the Stack"
        else:
            # Return the top element from the stack without popping
            return self.list[-1]

    # Delete (Clear)
    def delete(self):
        # Clear the entire stack by assigning an empty list to it
        self.list = None

# Example usage:
my_stack = Stacks(maxsize=4)
my_stack.push(32)
my_stack.push(42)
my_stack.push(362)
print(my_stack)
print("Is the stack full?", my_stack.isfull())
my_stack.push(2)
print("Is the stack full?", my_stack.isfull())
