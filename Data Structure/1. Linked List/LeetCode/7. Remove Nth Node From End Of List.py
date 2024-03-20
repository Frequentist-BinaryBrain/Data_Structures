#   https://leetcode.com/problems/remove-nth-node-from-end-of-list/
#   https://youtu.be/XVuQxVej6y8?si=zKGiBqFMnn_Qt7ty

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        dummy = ListNode(val=0, next=head)  # We will initialise dummy node before head
        left = dummy  # we will initialise left pointer at dummy node i.e before head
        right = head  # we will initialise right pointer at head node

        while n > 0 and right is not None:
            right = right.next  # if n == 2 then it will move those many places to next
            n -= 1  # decrease 1 for every iteration

        while right:
            left = left.next
            right = right.next

        # we will now remove the link for the node
        left.next = left.next.next
        return dummy.next
