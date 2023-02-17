# Leet code problem
# Given a string, return the length of the longest substring consisting of unique elements

class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:

        # Initialize substring and max length
        substr = ''
        length = 0

        # Empty string case
        if (len(s) == 0):
            return length

        for i in range(len(s)):

            # If next element in string appears in substring, delete everything up to
            # and including that element in substring
            if s[i] in substr:
                index = substr.index(s[i])+1
                substr = substr.replace(substr[0:index], '')
                substr += s[i]

            else:
                substr += s[i]
                if (len(substr) > length):
                    length = len(substr)
        return length
    
# Example to check
s = 'pwwkew'
print(Solution().lengthOfLongestSubstring(s))