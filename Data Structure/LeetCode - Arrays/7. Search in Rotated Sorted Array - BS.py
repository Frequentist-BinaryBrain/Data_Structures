#   https://leetcode.com/problems/search-in-rotated-sorted-array/
#   https://youtu.be/5qGrJbHhqFs?si=46Bkdtj6izeHOU-g


#     Understand the Problem: The problem involves searching for a target element in a rotated sorted array.
#
#     Identify the Sorted Half: Since the array is rotated, it's crucial to identify which half of the array is sorted.
#
#     Apply Binary Search: Utilize binary search to efficiently locate the target element. This involves repeatedly dividing the search
#     interval in half until the target is found or the interval is empty.
#
#     Check if Target is Found: If the target is found at the midpoint, return its index immediately.
#
#     Determine Sorted Half and Eliminate Unsorted Half: Based on the comparison of elements at the endpoints and midpoint of the search interval,
#     identify which half of the array is sorted. Then, eliminate the unsorted half of the array to focus the search on the sorted portion.
#
#     Update Pointers: Adjust the low and high pointers accordingly based on whether the target lies within the sorted half or the unsorted half.
#
#     Repeat Binary Search: Continue the binary search process until the target is found or the search interval is empty.
#
#     Return Result: If the target is found, return its index. If the target is not found, return -1.



class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        #   Since this is sorted, we will first go to mid point and check for one half
        #   Please identify the sorted half because we dont know which is sorted
        #   Then eliminate that unsorted half

        # Initialize pointers for binary search
        low, high = 0, len(nums) - 1

        # Perform binary search until low pointer is less than or equal to high pointer
        while low <= high:
            mid = (low + high) // 2  # Calculate mid index

            # Check if mid element is equal to target
            if nums[mid] == target:
                return mid

            # Check if left half is sorted
            if nums[low] <= nums[mid]:
                # Check if target lies within left half
                if nums[low] <= target < nums[mid]:  # Target lies in sorted left half
                    high = mid - 1  # Update high pointer to mid - 1
                else:
                    low = mid + 1  # Update low pointer to mid + 1 because target lies in right half
            # Right half is sorted
            else:
                # Check if target lies within right half
                if nums[mid] < target <= nums[high]:  # Target lies in sorted right half
                    low = mid + 1  # Update low pointer to mid + 1
                else:
                    high = mid - 1  # Update high pointer to mid - 1 because target lies in left half

        # If target is not found, return -1
        return -1
