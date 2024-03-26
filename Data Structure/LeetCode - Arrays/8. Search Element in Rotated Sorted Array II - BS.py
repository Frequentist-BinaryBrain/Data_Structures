#   https://youtu.be/w2G2W8l__pc?si=-8j9fTaf3VDJJgDq
#   https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

#   Identify the sorted half: Similar to the case with unique elements, the first step is to identify which half of the array is sorted.
#   This step is crucial for determining where to search for the target.
#
# Handle duplicate elements: Since the array can contain duplicates, comparing the elements at both ends and the middle might not always help identify
# the sorted half. In cases where nums[low] == nums[mid] == nums[high], the typical binary search approach might not work efficiently.

# Index:   0  1  2  3  4  5
# Array: [ 3, 2, 3, 4, 1, 3]
#          ↑              ↑
#         low           high
#                ↑
#               mid

# Shrink the search space: When nums[low] == nums[mid] == nums[high], you cannot determine the sorted half based on comparisons alone.
# Therefore, shrink the search space by incrementing low and decrementing high until you can distinguish between the sorted and unsorted halves.

# Index:   0  1  2  3  4  5
# Array: [ 3, 2, 3, 4, 1, 3]
#             ↑        ↑
#           low       high
#                ↑
#               mid
#
# Continue searching: After shrinking the search space, continue with the binary search approach by updating pointers based on comparisons with the target value.
#
# Repeat the process if needed: If the condition nums[low] == nums[mid] == nums[high] persists after shrinking the search space, repeat the process until
# the condition no longer holds or until the search space becomes empty.
#
# Handle edge cases: Consider edge cases where the array contains only duplicates or where the duplicates are spread across the array.
# Test your solution with such cases to ensure correctness.


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        # Get the length of the input array
        n = len(nums)

        # Initialize pointers for binary search
        low, high = 0, n-1

        # Binary search loop
        while low <= high:
            # Calculate the mid-index
            mid = (low + high) // 2

            # If the target is found at the mid index, return True
            if nums[mid] == target:
                return True

            # If nums[low], nums[mid], and nums[high] are all equal, adjust pointers
            if nums[mid] == nums[high] == nums[low]:
                low += 1
                high -= 1
                continue

            # Check if the left half is sorted
            if nums[low] <= nums[mid]:
                # Check if the target is within the sorted left half
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

            else:  # Right half is sorted
                # Check if the target is within the sorted right half
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        # If the target is not found, return False
        return False
