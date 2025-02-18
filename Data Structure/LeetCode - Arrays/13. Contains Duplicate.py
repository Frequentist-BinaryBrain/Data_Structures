#   https://leetcode.com/problems/contains-duplicate/description/


class Solution(object):
    def containsDuplicate(nums):
        # Initialize an empty set to store encountered elements
        hashset = set()

        # Iterate through each element in the list
        for i in nums:
            # If the current element is already in the set, it means it's a duplicate
            if i in hashset:
                # Return True to indicate the presence of duplicates
                return True
            else:
                # If the current element is not in the set, add it to the set
                hashset.add(i)

        # If no duplicates are found after iterating through the entire list, return False
        return False
