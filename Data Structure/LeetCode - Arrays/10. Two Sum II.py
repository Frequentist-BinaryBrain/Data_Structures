#   https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

#     Iterate through the numbers list using enumerate() to get both the index and the number.
#     Calculate the difference diff between the target and the current number.
#     Check if diff exists in the hash map. If it does, return the indices of the current number (stored in hash[diff]) and the current index plus one (since the indices are 1-indexed).
#     If diff doesn't exist in the hash map, store the current number along with its index in the hash map.
#     If no such pair is found after iterating through all numbers, return an empty list.


class Solution(object):
    def twoSum(self, numbers, target):
        """
        Finds two numbers in the list 'numbers' that add up to the given target.

        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Create a dictionary to store the indices of numbers encountered so far
        hash = {}

        # Iterate through the numbers list with their indices
        for index, num in enumerate(numbers):

            # Calculate the difference needed to reach the target
            diff = target - num

            # Check if the difference exists in the hash (i.e., if a pair is found)
            if diff in hash:
                # If a pair is found, return the indices of the pair (adjusted by 1)
                return [hash[diff] + 1, index + 1]
            else:
                # Store the current number along with its index in the hash
                hash[num] = index

        # If no such pair is found, return an empty list
        return []
