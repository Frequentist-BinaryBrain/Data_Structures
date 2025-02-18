# https://leetcode.com/problems/valid-anagram/




class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count_s = {}
        count_t = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            # count_s.get(i, 0): Gets the count of occurrences of the character s[i] from the dictionary count_s.
            # If s[i] is not found in the dictionary count_s, it returns 0.
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)

        return count_s == count_t
