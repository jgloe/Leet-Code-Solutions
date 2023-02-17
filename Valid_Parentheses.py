# Leet code problem
# Given a string of parentheses, determine if the string is valid

class Solution:

    def __init__(self):
        self.name = 'Solution'

    def isValid(self, s):

        # Replace open-close parentheses, looping until exhausted
        while (s != ''):
            temp = s.replace('()', '')
            temp = temp.replace('[]', '')
            temp = temp.replace('{}', '')
            if (temp == s):
                return (s == '')
            else:
                s = temp
        return True
    
# Example to check
s = '[([]])'
print(Solution().isValid(s))