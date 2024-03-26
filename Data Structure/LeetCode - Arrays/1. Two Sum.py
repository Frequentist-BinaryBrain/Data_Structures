#   https://leetcode.com/problems/two-sum/
#   https://youtu.be/KLlXCFG5TnA?si=4Q9cDc0ygjGqEamN

class Solution:  #
    # def twoSum(self, nums, target):
    #     # Brute force solution O(n^2)

    #     # Initialize an empty list to store pairs of indices
    #     empty = []

    #     # Iterate through each element in the nums list using its index
    #     for i in range(len(nums)):
    #         # Iterate through the elements after the current element
    #         # This ensures that each pair (i, j) is considered only once
    #         for j in range(i+1, len(nums)):
    #             # Check if the sum of the elements at indices i and j equals the target
    #             if nums[i] + nums[j] == target:
    #                 # If the sum equals the target, append the pair (i, j) to the empty list
    #                 empty.append(i)
    #                 empty.append(j)

    #     # Return the list containing pairs of indices whose elements sum up to the target
    #     return empty

    def twoSum(self, nums, target):
        # Create a dictionary to store the mapping of values to their indices
        preHash = {}  # Format: {value: index}

        # Iterate through each element in the nums list along with its index
        for i, n in enumerate(nums):
            # Calculate the difference between the target value and the current element
            diff = target - n

            # Check if the difference exists in the preHash dictionary
            if diff in preHash:
                # If the difference exists, it means we have found a pair of indices
                # whose elements sum up to the target
                # Return the indices of the current element and the element found in preHash
                return [preHash[diff], i]
            else:
                # If the difference doesn't exist in preHash,
                # store the current element's value and its index in the preHash dictionary
                preHash[n] = i

        # If no such pair is found in the nums list, return an empty list
        return



