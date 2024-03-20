#   https://leetcode.com/problems/merge-two-sorted-lists/description/
#   https://youtu.be/XIdigk956u0?si=7iTA5GdlZQ4Oq6hr

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        newHead = dummyHead = ListNode() # this is the new list where we add sorted numbers from l1 and l2


        while list1 and list2:
            if list1.val < list2.val:
                dummyHead.next = list1
                list1 = list1.next
            else:
                dummyHead.next = list2
                list2 = list2.next
            dummyHead = dummyHead.next

            # What if one of the list has more elements left i.e. not null
            # i.e list1 = [1,2,4,6,7], list2 = [1,3,4]
            # Since list1 has extra 2 number we will add them below
        if list1:
            dummyHead.next = list1
        if list2:
            dummyHead.next = list2
        return newHead.next







