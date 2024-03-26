#   https://leetcode.com/problems/3sum/description/


# This uses hash but exceeds time limit when submits into leet code because of O(n^2)
class Solution(object):
    def threeSum(self, nums):
        """
        Finds all unique triplets in the list 'nums' such that the sum is zero.

        :type nums: List[int]
        :rtype: List[List[int]]
        """

        hash = {}
        n = len(nums)
        result = []

        # Build a hash map to store the index of each number
        for index, num in enumerate(nums):
            hash[num] = index

        # Iterate through the list to find triplets
        for i in range(n):
            for j in range(i + 1, n):
                # a + b + c = 0
                # c = -(a + b)
                # Calculate the third number needed to form a triplet that sums up to zero
                desired = -(nums[i] + nums[j])
                # Check if the desired number exists in the hash map and its index is different from i and j
                if desired in hash and hash[desired] != i and hash[desired] != j:
                    # Create a sorted list containing the triplet
                    triplet = sorted([nums[i], nums[j], desired])
                    # Add the triplet to the result if it's not already present
                    if triplet not in result:
                        result.append(triplet)

        return result




# Two pointer

class Solution(object):
    def threeSum(self, nums):
        """
        Finds all unique triplets in the list 'nums' such that the sum is zero.

        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()  # Sort the input list
        n = len(nums)
        result = []

        # Iterate through the list
        for i in range(n - 2):
            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Use two pointers to find the other two elements
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    # Skip duplicate values for the second element
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicate values for the third element
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result

# Different way

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def find_two(nums, i):
            left, right = i + 1, len(nums) - 1
            while (left < right):
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while(left < right) and nums[left] == nums[left - 1]:
                        left += 1

        result = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break;

            if i == 0 or nums[i-1] != nums[i]:
                find_two(nums, i)

        return result

