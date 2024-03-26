#   https://leetcode.com/problems/maximum-subarray/
#   https://youtu.be/5WZl3MMT0Eg?si=m74Mh5NHpA8Le6IM

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Initialize variables to keep track of maximum sum and current sum
        maxSum = nums[0]  # Initialize maxSum with the first element of nums
        cur_sum = 0  # Initialize cur_sum to 0

        # Iterate through each element in the nums array
        for n in nums:
            # If the current sum is negative, reset it to 0
            if cur_sum < 0:
                cur_sum = 0
            # Add the current element to the current sum
            cur_sum += n
            # Update maxSum to be the maximum of maxSum and current sum
            maxSum = max(maxSum, cur_sum)

        # Return the maximum sum
        return maxSum