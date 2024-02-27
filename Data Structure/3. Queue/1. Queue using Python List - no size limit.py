# Implementation

# 1. Python List
#   - Queue without capacity - A queue without capacity means that the queue can grow dynamically without any predefined limit
#   - Queue with capacity (Circular Queue) - A circular queue is a variation where the front and rear pointers move in a circular fashion.
#                                            Once the rear reaches the end, it wraps around to the beginning. This allows for efficient use of space and avoids the need to shift elements
#                                            when the rear pointer reaches the end. It is particularly useful when the underlying storage has a fixed size.

# 2. Linked List:  The front of the queue is represented by the head of the linked list, and the rear is represented by the tail.
#                  Elements are added to the rear and removed from the front, maintaining the FIFO order.

#  -----------------------
# | Queue without capacity |
#  ------------------------
class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return ''.join(values)

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False
    def enqueue(self, value):
        self.items.append(value)
        return f"The element {value} is inserted at the end of Queue"

    def dequeue(self):
        if self.isEmpty():
            return "This is already empty"
        else:
            self.items.pop(0)

    def peek(self):
        if self.isEmpty():
            return "This is already empty"
        else:
            return self.items[0]

    def delete(self):

        self.items = None




custom_queue = Queue()
print(custom_queue.isEmpty())
print(custom_queue.enqueue(2))
print(custom_queue.isEmpty())
print(custom_queue.enqueue(12))
print(custom_queue.dequeue())
print(custom_queue)
print("Peeked item is:", custom_queue.peek())
print(custom_queue.delete())


