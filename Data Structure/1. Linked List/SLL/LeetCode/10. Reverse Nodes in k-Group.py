#  https://youtu.be/1UOPsfP85V4?si=amZnOQmzgY_M5_v3
# https://leetcode.com/problems/reverse-nodes-in-k-group/


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        # Initialize a dummy node with value 0 and next pointing to the head of the linked list
        dummy_node = ListNode(0, head)

        # Initialize a pointer 'groupPrev' which will point to the node before the start of each group
        groupPrev = dummy_node

        # Loop until all groups have been reversed
        while True:
            # Get the kth node from the current 'groupPrev'
            kth = self.getKth(groupPrev, k)

            # If 'kth' is None, that means we reached the end of the list or
            # the remaining nodes are not big enough to form a complete group of size 'k'
            if not kth:
                break

            # 'groupNext' points to the node immediately after the kth node
            groupNext = kth.next

            # Reverse the group of nodes
            prev = kth.next  # 'prev' initially points to the node after kth
            curr = groupPrev.next  # 'curr' points to the first node in the group

            while curr != groupNext:
                tmp = curr.next  # Temporary pointer to store the next node
                curr.next = prev  # Reverse the pointer of 'curr' to point to 'prev'
                prev = curr  # Move 'prev' pointer forward
                curr = tmp  # Move 'curr' pointer forward

            # 'tmp' now holds the first node of the reversed group
            tmp = groupPrev.next

            # 'groupPrev' now needs to point to the last node of the reversed group
            groupPrev.next = kth

            # Move 'groupPrev' to the first node of the next group
            groupPrev = tmp

        # Return the modified linked list, excluding the dummy node
        return dummy_node.next

    # Helper function to get the kth node from the given node 'curr'
    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
