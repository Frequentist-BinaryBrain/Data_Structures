# In python we can create queue using 3 different modules i.e
# 1. Queue module:  This module provides the Queue class, which is a basic implementation of a FIFO (First-In-First-Out) queue
# 2. Collection module: The collections module provides the deque (double-ended queue) class, which can be used to implement a queue.
# 3. multiprocessing module: The multiprocessing module provides a Queue class specifically designed for communication between processes

# -------------------
# Collection module:|
# -------------------

#  The Queue class in the collections module provides a basic implementation of a FIFO (First-In-First-Out) queue.
#  It is a simple and thread-safe queue, making it suitable for communication between threads within a single process.
#  The Queue class is especially useful in scenarios where multiple threads need to share data and synchronize their operations.

#   NOTE: ------------
#   When you append a new element to a deque with a maxlen, if the deque is already at its maximum length,
#   it will automatically remove elements from the opposite end to make space for the new element. This creates a sliding window effect.


from collections import deque

# To Enqueue elements to queue - APPEND
# To Dequeue elements from the queue - POPLEFT
# To delete all the elements from queue  - CLEAR

customQueue = deque(maxlen=3)
print(customQueue)
print("---------------")
customQueue.append(1)
customQueue.append(2)
customQueue.append(3)
print(customQueue)
print("---------------")
customQueue.append(4)
print(customQueue)
print("---------------")
print(customQueue.popleft())
print(customQueue)
print("---------------")
print(customQueue.clear())
print(customQueue)
print("---------------")


# --------------
# Queue module:|
# --------------

#   The Queue class in the Queue module (often referred to as queue.Queue) is a basic implementation of a FIFO (First-In-First-Out) queue in Python.
#   This class is part of the standard library and is commonly used for thread-safe communication between different parts of a program or threads.

#   1. qsize()
#
#     Description: Returns the approximate size (number of elements) of the queue.
#
# 2. empty()
#
#     Description: Returns True if the queue is empty, False otherwise.
#
# 3. full()
#
#     Description: Returns True if the queue is full, False otherwise. Note: Not all queues support being full.
#
# 4. put(item, block=True, timeout=None)
#
#     Description: Enqueues (puts) an item into the queue.
#     Parameters:
#         item: The item to be enqueued.
#         block: If True (default), blocks if the queue is full. If False, raises an exception.
#         timeout: Time to wait if block is True before raising an exception.
#
# 5. get(block=True, timeout=None)
#
#     Description: Dequeues (gets) an item from the queue.
#     Parameters:
#         block: If True (default), blocks if the queue is empty. If False, raises an exception.
#         timeout: Time to wait if block is True before raising an exception.
#
# 6. task_done()
#
#     Description: Indicates that a previously enqueued task is complete. Used with join().
#
# 7. join()
#
#     Description: Blocks until all items in the queue have been gotten and processed. Typically used with task_done() to wait for completion.

import queue as q

customQueue = q.Queue(maxsize=3)
print(customQueue.qsize())
print(customQueue.empty())
print("---------------")
customQueue.put(1)
customQueue.put(10)
customQueue.put(100)
print(customQueue.qsize())
print("---------------")
print(customQueue.full())
print("---------------")
print(customQueue.get())
customQueue.put(100)
print(customQueue)


# -----------------------
# Multiprocessing module:|
# -----------------------

# It used for sharing data between processors and can store any object

from multiprocessing import Queue
customQueue = Queue(maxsize=3)
customQueue.put(1)
print(customQueue.get(1))

#   Except task done and join method we can use previous Queue module methods over here
