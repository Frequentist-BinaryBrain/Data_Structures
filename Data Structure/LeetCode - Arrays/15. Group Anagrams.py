# https://leetcode.com/problems/group-anagrams/

class Solution(object):
    def groupAnagrams(self, strs):
        # Create a hashmap to store groups of anagrams
        anagrams = {}

        # Iterate through each string in the input array
        for s in strs:
            # Sort the characters of the string to get a unique key
            sorted_s = ''.join(sorted(s))
            # sorted(s): This part sorts the characters of the string s in lexicographic (alphabetical) order. For example, if s = "eat", sorted(s) would return ['a', 'e', 't'].
            # ''.join(...): This part joins the sorted characters back together into a single string.
            # The empty string '' is used as a separator. So, for the sorted list ['a', 'e', 't'], ''.join(['a', 'e', 't']) would return 'aet'.

            # Check if the sorted string exists as a key in the hashmap
            # If not, create a new key-value pair with an empty list as the value
            if sorted_s not in anagrams:
                anagrams[sorted_s] = []

            # Append the original string to the list corresponding to the sorted key
            anagrams[sorted_s].append(s)

        # Return the values of the hashmap as a list of lists
        sorted_groups = sorted(anagrams.values(), key=lambda x: x[0])

        # Return the sorted groups
        return sorted_groups

        #   In the context of this problem, each group is a list of strings (anagrams).
        # We want to sort these groups based on the first string in each group. So, the lambda function
        # lambda x: x[0] extracts the first string from each group, which serves as the sorting criterion.
        # The sorted() function then sorts the list of groups based on this criterion.
