#   https://leetcode.com/problems/middle-of-the-linked-list/
#   https://youtu.be/A2_ldqM4QcY?si=XzS645HJLakEydSZ


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        Find the middle node of a singly linked list.

        :type head: ListNode
        :rtype: ListNode
        """
        # If the list is empty or contains only one node, return the head
        if not head or not head.next:
            return head

        # Initialize two pointers: slow and fast
        slow = head
        fast = head

        # Traverse the list until the fast pointer reaches the end (or None)
        # If the number of nodes is even, fast.next.next will be None when fast reaches the end
        # If the number of nodes is odd, fast.next will be None when fast reaches the end
        while fast and fast.next:
            # Move slow pointer one step forward
            slow = slow.next
            # Move fast pointer two steps forward
            fast = fast.next.next

        # Return the node pointed by the slow pointer, which is the middle node
        # If the number of nodes is even, slow points to the second middle node
        # If the number of nodes is odd, slow points to the middle node
        return slow
