
#   https://youtu.be/S5bfdUTrKLM?si=C5JR-AbLzmZ3HQzB
#   https://leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """

        """
        1. Find the middle of the linked list.
        2. Reverse the second half of the linked list.
        3. Merge the first half and the reversed second half alternatively.
        """

        # We have to find the middle of the list first
        slow, fast = head, head.next

        # Find the middle using slow and fast pointers
        while fast and fast.next:
            slow = slow.next  # Slow pointer moves one step
            fast = fast.next.next  # Fast pointer moves two steps

        # 'slow' now points to the middle node.
        # 'second' will point to the beginning of the second half of the list.
        second = slow.next
        slow.next = None  # Break the link to split into two lists

        # Now we need to reverse the second half of the list
        prev = None  # Initialize a pointer to None
        while second:
            tmp = second.next  # Store next node to avoid losing it
            second.next = prev  # Reverse the link
            prev = second  # Move 'prev' pointer forward
            second = tmp  # Move 'second' pointer forward

        # 'prev' now points to the head of the reversed second half.

        # Merge the two halves of the list alternatively
        first, second = head, prev  # Pointers to the heads of both halves
        while second:
            tmp1, tmp2 = first.next, second.next  # Store next nodes
            first.next = second  # Link the nodes alternatively
            second.next = tmp1
            first, second = tmp1, tmp2  # Move pointers forward to next nodes
