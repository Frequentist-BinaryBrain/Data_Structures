#   https://leetcode.com/problems/top-k-frequent-elements/description/


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Dictionary to store frequency counts of elements
        freq_map = {}

        # Count frequency of each element
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        # Sort the dictionary by values in descending order
        sorted_freq = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)

        # Extract top k frequent elements
        top_k = [pair[0] for pair in sorted_freq[:k]]

        return top_k




# Example for the code line

freq_map = {1: 3, 2: 2, 3: 1}
sorted_freq = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)

print(sorted_freq)

#output:

[(1, 3), (2, 2), (3, 1)]

#   In this example:
#   In Python, when you call the items() method on a dictionary, it returns a view object that displays a list of tuple pairs.
#
#     The key-value pairs in freq_map are {1: 3, 2: 2, 3: 1}.
#     After sorting freq_map.items() by the values in descending order, we get [(1, 3), (2, 2), (3, 1)] as the result.
#     Each tuple in sorted_freq consists of an element and its frequency count. For example, (1, 3) means that the element 1 appears 3 times in the original list nums.
#
# So, sorted_freq is a list of tuples where each tuple contains an element and its frequency count, sorted by frequency in descending order.


# sorted_freq[:k]: This expression takes a slice of the list sorted_freq, starting from index 0 (the first element) and ending just before index k.
#
# So, sorted_freq[:k] extracts the first k elements from the sorted_freq list.
#
# For example, if sorted_freq is [(1, 3), (2, 2), (3, 1)] and k = 2, then sorted_freq[:k] would be [(1, 3), (2, 2)], as it takes the first two elements of the list sorted_freq.
#
# In the context of the problem, sorted_freq[:k] is used to extract the top k frequent elements from the sorted list of tuples sorted_freq, which represents elements and their frequencies.
