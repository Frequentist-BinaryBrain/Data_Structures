#   https://youtu.be/nhEMDKMB44g?si=-MIfXoJODn-Pz9y-
#   https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

#     Identify Sorted Half: Determine whether the left or right half of the array is sorted.
#     Apply Binary Search: Use binary search to find the minimum element
#     Eliminate Sorted Half: Since the minimum element can only be present in the unsorted half, eliminate the sorted half from consideration.
#     Update Minimum: Update the minimum element found so far if necessary.
#     Repeat or Terminate: Repeat the process with the remaining portion of the array, or terminate if the minimum element has been found.



class Solution(object):
    def findMin(self, nums):
        """
        Finds the minimum element in a rotated sorted array.

        :type nums: List[int]
        :rtype: int
        """

        # Initialize variables
        n = len(nums)  # Length of the input array
        low, high = 0, n - 1  # Initialize low and high indices for binary search
        answer = float('inf')  # Initialize answer to positive infinity

        # Perform binary search
        while low <= high:
            mid = (low + high) // 2  # Calculate middle index

            if nums[mid] <= nums[high]:  # If right half is sorted
                answer = min(answer, nums[mid])  # Update answer with minimum in right half
                high = mid - 1  # Move high pointer to mid - 1 to eliminate right half
            else:  # If left half is sorted
                answer = min(answer, nums[low])  # Update answer with minimum in left half
                low = mid + 1  # Move low pointer to mid + 1 to eliminate left half

        return answer
