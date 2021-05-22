class Solution(object):
    def numIdenticalPairs(self, nums):
        c = 0
        for i in range(len(nums)):
            print(i)
            print(nums[:i])
            c += nums[:i].count(nums[i])
        return c


obj = Solution()
print(obj.numIdenticalPairs([1,2,3,1,1,3]))
