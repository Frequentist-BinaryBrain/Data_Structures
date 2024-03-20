# Definition for singly-linked list.
#    https://leetcode.com/problems/add-two-numbers/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()  # Resulting Linked List

        cur_pointer = dummy  # This is the pointer used to insert a new node or digit
        carry_digit = 0

        # We usually start adding from right side i.e. Ones digits place, since reverse
        # We will add from head i.e. from left
        while l1 or l2 or carry_digit:  # We will iterate as long as they are not Null
            # We will take else 0 because if there is no element on right corner side we will add 0
            # 3 5 5   <---- we will put zero in these cases
            # 5 6 6 6

            v1 = l1.val if l1 is not None else 0
            v2 = l2.val if l2 is not None else 0

            # Addition of the above two digits to get a sum, dont forget to add carry
            val = v1 + v2 + carry_digit
            # what if result is to digits of above addition
            carry_digit = val // 10
            # we need only one place digit so we mod it
            val = val % 10
            cur_pointer.next = ListNode(val)  # Inserting into the new node dummy we created

            # update pointers
            cur_pointer = cur_pointer.next
            l1 = l1.next if l1 else None  # Updating l1 and l2 pointers if not null
            l2 = l2.next if l2 else None
        return dummy.next

        #   After the addition process is complete, the actual head of the resulting linked list is the
        # node immediately after the dummy node. Therefore, dummy.next points to the actual head of the
        # resulting linked list.
