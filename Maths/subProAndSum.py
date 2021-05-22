class Solution(object):
    def subtractProductAndSum(self, n):
        sum = 0
        product = 1
        number = str(n)
        for i in number:
            sum += int(i)
            product *= int(i)
        return product - sum


obj = Solution()
print(obj.subtractProductAndSum(4421))