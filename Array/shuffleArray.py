class Solution(object):
    def shuffle(self, nums, n):
        array = []
        for i in range(n):
            array.append(nums[i])
            array.append(nums[i+n])
        return array

obj = Solution()
print(obj.shuffle([2, 5, 1, 3, 4, 7], 3))