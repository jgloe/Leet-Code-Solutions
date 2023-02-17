# Leet code problem
# Given a string, determine the longest palindromic substring

class Solution:

    def __init__(self):
        self.name = 'Solution'

    def longestPalindrome(self, s: str) -> str:

        substr = ''
        i = 1
        while (i < len(s) - len(substr) - 1):
            j = 1
            while (i-j >= 0) and (i+j < len(s)):
                print('i = ' + str(i))
                print('j = ' + str(j))
                if (s[i-j] == s[i+j]):
                    j += 1
                    if (2*j > len(substr)):
                        substr = s[(i-j):(i+j+1)]
                else:
                    i += 1
                    break

        i = int((len(substr)-1)/2)
        while (i < len(s) - len(substr) - 1):
            j = 1
            while (i-j+1 >= 0) and (i+j < len(s)):
                if (s[i-j+1] == s[i+j]):
                    j += 1
                    if (2*j - 1 > len(substr)):
                        substr = s[(i-j+1):(i+j+1)]
                else:
                    i += 1
                    break

        return substr
    
s = 'bcbbabca'
print(Solution().longestPalindrome(s))
