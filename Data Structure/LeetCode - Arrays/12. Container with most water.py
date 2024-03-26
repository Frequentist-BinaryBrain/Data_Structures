#   https://leetcode.com/problems/container-with-most-water/




class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        # Initialize pointers at both ends of the array
        left_pointer = 0
        right_pointer = len(height) - 1
        max_area = 0  # Variable to store the maximum area found

        # Loop until the pointers meet each other
        while left_pointer < right_pointer:
            # Calculate the height of the current container (minimum of the two heights)
            h = min(height[left_pointer], height[right_pointer]) #  because water cant flow over min point until max
            # Calculate the width of the container
            w = right_pointer - left_pointer

            # Calculate the area of the current container
            area = w * h
            # Update max_area if the area of the current container is greater
            max_area = max(area, max_area)

            # Move the pointer that points to the smaller height towards the center
            # This is because the area of a container is limited by the shorter side
            if height[left_pointer] > height[right_pointer]:
                right_pointer -= 1
            else:
                left_pointer += 1

        # Return the maximum area found
        return max_area

