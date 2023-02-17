# Leet code problem
# Given a list of strings, find the longest common prefix among them

class Solution:

    def __init__(self):
        self.name = 'Solution'

    def longestCommonPrefix(self, strs):

        prefix = ''
        smstr = min(strs, key=len)

        #Check if list is empty
        if (len(smstr) == 0):
            return prefix

        # Initialize array
        arr = [[] for i in range(len(strs))]

        # Decompose each string in list into individual letters
        for i in range(len(strs)):
            temp_list = list(strs[i])
            arr[i] = temp_list[0:len(smstr)]

        # Check if each letter matches the others in the list
        for j in range(len(smstr)):
            if (len(set([item[j] for item in arr])) != 1):
                return prefix
            else:
                prefix = prefix + arr[0][j]

# Example to test
strs = ["flower","flow","flight"]
print(Solution().longestCommonPrefix(strs))
