
# https://leetcode.com/problems/reverse-linked-list/description/


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    #   https://youtu.be/G0_I-ZF0S38?si=okkPDhk9M1k2bI-Z

class Solution(object):

    def reverseList(self, head):


        # Initialize prev_node to None, indicating the end of the reversed list
        prev_node = None
        # Initialize curr_node to the head of the original list
        curr_node = head

        # Traverse the original list
        while curr_node:
            # Store the next node of the current node
            next_node = curr_node.next
            # Reverse the pointer of the current node to point to the previous node
            curr_node.next = prev_node
            # Move prev_node and curr_node one step forward
            prev_node = curr_node
            curr_node = next_node

        # After the loop, prev_node will point to the new head of the reversed list
        # Return prev_node as it now represents the head of the reversed list
        return prev_node



