"""
Given a string s, find the length of the longest substring without repeating characters.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if 0 <= len(s) <= 1:
            return len(s)

        length = 0
        counter = 0
        unique_chars = ''

        for i in range(len(s)):
            for char in s[i:]:
                if char not in unique_chars:
                    unique_chars += char
                    counter += 1
                else:
                    length = max(counter, length)
                    unique_chars = ''
                    counter = 0
                    break

        return length


a = Solution()
print(a.lengthOfLongestSubstring('abcabcbb'))
print(a.lengthOfLongestSubstring('bbbbb'))
print(a.lengthOfLongestSubstring('pwwkew'))
print(a.lengthOfLongestSubstring(''))
