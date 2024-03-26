# https://leetcode.com/problems/contains-duplicate-ii/


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # Dictionary to store the indices of encountered elements
        num_indices = {}

        # Iterate through the array with indices using enumerate
        for i, num in enumerate(nums):
            # Check if the current element is already in the dictionary
            if num in num_indices:
                # If it is, check if the absolute difference between
                # the current index and the index stored in the dictionary
                # for that element is less than or equal to k
                if abs(i - num_indices[num]) <= k:
                    # If it is, return True, as we found a pair of indices
                    # with the same element and the difference is within k
                    return True
            # Update the dictionary with the current index for the element
            num_indices[num] = i

        # If no such pair is found after iterating through the array,
        # return False
        return False