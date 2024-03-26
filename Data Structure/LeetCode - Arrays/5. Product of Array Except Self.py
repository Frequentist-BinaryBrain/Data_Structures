# https://leetcode.com/problems/product-of-array-except-self/description/
# https://youtu.be/bNvIQI2wAjk?si=MNz8pgNrBz3oQ1J7

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Initialize result array with ones, same length as input nums
        result = [1] * len(nums)

        # Calculate prefix products
        prefix_product = 1
        for i in range(len(nums)):
            # Multiply current result by prefix product
            result[i] *= prefix_product
            # Update prefix product for the next iteration
            prefix_product *= nums[i]

        # Calculate suffix products
        suffix_product = 1
        for i in range(len(nums) - 1, -1, -1):
            # Multiply current result by suffix product
            result[i] *= suffix_product
            # Update suffix product for the next iteration
            suffix_product *= nums[i]

        # Return the result array
        return result
