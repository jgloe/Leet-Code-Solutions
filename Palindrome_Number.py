# Leet code problem
# Given an input integer, return if the input is a palindrome

class Solution:

    def __init__(self):
        self.name = 'Solution'

    def isPalindrome(self, x):
        # Convert integer to string
        st = str(x)

        # Loop over half string and check symmetric values
        for i in range(int(len(st)/2)):
            if st[i] != st[len(st)-1-i]:
                return False
        return True

# Test Example
x = 1231
print(Solution().isPalindrome(x))