class Queue:
    def __init__(self, maxsize):
        # Create a list to store queue elements, initialized to None
        self.items = maxsize * [None]

        # Set the maximum size (capacity) of the circular queue
        self.maxsize = maxsize
        # When the start and top pointers are both -1, it means the queue is empty.
        # When you enqueue (add an element), you move the top pointer forward.
        # If the queue was empty before, you set both start and top to 0.
        # Initialize start and top pointers to -1 when the queue is empty
        self.start = -1
        self.top = -1

    def __str__(self):
        # Filter out None values and convert each non-None element to a string
        values = [str(x) for x in self.items if x is not None]

        return ''.join(values)


    def isfull(self):
        # Check if the next position after the top pointer is the same as the start pointer,
        # or if both start and top pointers are at the maximum capacity (circular queue is full)
        if (self.top + 1 == self.start) or ((self.start == self.maxsize) and (self.top + 1 == 0)):
            return True
        else:
            return False

    def isEmpty(self):
        # Check if the top pointer is -1, indicating that the queue is empty
        if self.top == -1:
            return True
        else:
            return False

    def Enqueue(self, value):
        if self.isfull():
            return "This Queue is full"
        else:
            # Check if the top pointer is at the maximum capacity, wrap around to the beginning
            if self.top + 1 == self.maxsize: # because top is the end of list and we will move it to first spot again
                self.top = 0
            else:
                # Increment the top pointer, set start to 0 if it was -1 (queue was empty)
                self.top += 1
                if self.start == -1:
                    self.start = 0
            # Insert the value at the position of the top pointer in the items list
            self.items[self.top] = value
            return f"The element {value} is inserted at the end of the queue"

#   Whenever we are calling Enqueue method we are changing top variable and whenever
#   we are calling Dequeue we will change the start variable to next


    def Dequeue(self):
        # Check if the queue is empty
        if self.isEmpty():
            return "There is no element in the stack to dequeue"
        else:
            # Store the first element to be dequeued in a temporary variable
            firstElement = self.items[self.start]
            start = self.start  # So we can remove this later

            # Check if this is the only element in the queue
            if self.start == self.top:
                # If yes, set start and top to -1 to indicate an empty queue after dequeuing
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.maxsize:
                # If the first element points to the last element, reset start to the beginning
                self.start = 0
            else:
                # Increment the start index to point to the next element in the queue
                self.start += 1

            # Set the original location of the dequeued element to None, effectively removing it
            self.items[start] = None

            # Return the dequeued element
            return firstElement

    def peek(self):
        if self.isEmpty():
            return "There is no element in the stack to dequeue"
        else:
            return self.items[self.start]

    def delete(self):
        # Set the entire items list to be a new list of None values with the length of maxsize
        self.items = self.maxsize * [None]

        # Reset start and top to -1, indicating an empty queue after deletion
        self.start = -1
        self.top = -1

        # The queue has been effectively cleared, and all previous elements are deleted
        # Any existing elements in the queue are replaced by a new list of None values
        # This method creates a fresh, empty queue


customQueue = Queue(3)
print(customQueue.isfull())
print(customQueue.isEmpty())
print(customQueue.Enqueue(32))
print(customQueue)

