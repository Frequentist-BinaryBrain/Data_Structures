#   https://youtu.be/q5a5OiGbT6Q?si=vL291v-_4Q57gliX
#   https://youtu.be/q5a5OiGbT6Q?si=vL291v-_4Q57gliX

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # Check if the input list of lists is empty or not
        if not lists or len(lists) == 0:
            return None

        # Iterate until there is only one list left in the 'lists' array
        while len(lists) > 1:
            mergedList = []
            # Merge pairs of lists in 'lists' and append them to 'mergedList'
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedList.append(self.mergeLists(l1, l2))
            # Update 'lists' with the merged lists
            lists = mergedList

        # Return the single merged list remaining in 'lists'
        return lists[0]

    # Helper function to merge two sorted linked lists
    def mergeLists(self, l1, l2):
        # Create a dummy node to serve as the head of the merged list
        dummy = ListNode()
        # 'tail' will point to the last node of the merged list
        tail = dummy

        # Traverse both lists and merge them
        while l1 and l2:
            # Compare the values of the current nodes of l1 and l2
            # Append the smaller node to the merged list and move to the next node
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            # Move tail to the last node of the merged list
            tail = tail.next

        # Append the remaining nodes of l1 or l2 to the merged list
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        # Return the head of the merged list (excluding the dummy node)
        return dummy.next
