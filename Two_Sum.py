# Leet code problem
# Given an array of numbers and a target, return the indices in the array of the two numbers which add to the target

class Solution:

    def __init__(self):
        self.name = 'Solution'

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Loop over nums, exhausting all possible pairs
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):

                # Check if sums yield the target
                if (nums[i] + nums[j] == target):
                    return [i, j]

        # If no pair works, return no solution
        return 'No solution found.'

# Example 1
nums = [2, 7, 11, 15]
target = 9
sol = Solution().twoSum(nums, target)
print(sol)

# Example 2
nums = [3, 2, 4]
target = 6
sol = Solution().twoSum(nums, target)
print(sol)