# Leet code problem
# Given a list and a target, return the index of where the target should be located in the list

class Solution:

    def searchInsert(self, nums: List[int], target: int) -> int:

        # Check edge cases
        if (nums[0] > target):
            return 0
        if (nums[len(nums)-1] < target):
            return len(nums)
        left = 0
        right = len(nums) - 1
        index = int((right - left) / 2)

        #Bisection method
        while (right - left > 1):
            if (nums[index] > target):
                right = index
                index = int((right + left) / 2)
            elif (nums[index] < target):
                left = index
                index = int((right + left) / 2)
            else:
                return index
        
        return index + 1