#   https://leetcode.com/problems/contains-duplicate/

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Create an empty set to store unique elements encountered so far
        empty = set()

        # Iterate through each element in the nums list
        for i in nums:
            # Check if the current element 'i' is already in the set 'empty'
            if i in empty:
                # If 'i' is already in the set, it means it's a duplicate
                # Return True to indicate that the nums list contains duplicates
                return True
            else:
                # If 'i' is not in the set, add it to the set 'empty'
                empty.add(i)

        # If no duplicates are found after iterating through all elements,
        # return False to indicate that the nums list does not contain duplicates
        return False