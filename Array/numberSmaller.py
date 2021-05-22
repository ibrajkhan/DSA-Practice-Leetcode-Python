class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        arrange = sorted(nums)
        array = []
        for i in range(len(nums)):
            position = arrange.index(nums[i])
            array.append(position)
        return array

obj = Solution()
print(obj.smallerNumbersThanCurrent([5,6,3,1,7,8,2,0]))