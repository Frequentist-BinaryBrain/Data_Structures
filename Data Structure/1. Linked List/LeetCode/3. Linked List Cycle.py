#   https://leetcode.com/problems/linked-list-cycle/
#   https://youtu.be/OQtvTZxA7-k?si=I05y8XfCcasRsraE
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        # Check if the linked list is empty or has only one node, as a cycle requires at least two nodes.
        if not head or not head.next:
            return False

        # Initialize two pointers: slow and fast.
        # slow starts at the head of the linked list, while fast starts at the next node.
        slow = head
        fast = head.next

        # Traverse the linked list using two pointers.
        # If there's a cycle, the fast pointer will eventually catch up with the slow pointer.
        while fast and fast.next:
            # Move slow pointer one step forward.
            slow = slow.next
            # Move fast pointer two steps forward.
            fast = fast.next.next

            # If slow and fast pointers meet at any point, there's a cycle.
            if slow == fast:
                return True

        # If the loop exits without finding a cycle, return False.
        return False




