# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.

class Solution(object):
    def runningSum(self, nums):
        count = 1
        while count<len(nums):
            nums[count] += nums[count-1]
            count += 1
        return print(nums)

obj = Solution()
obj.runningSum([1, 2, 3, 4])