class Solution(object):
    def maximum_wealth(self, accounts):
        wealth = 0
        array = []
        for i in accounts:
            for j in i:
                wealth += j
            array.append(wealth)
            wealth = 0
        largest_amount = 0
        for amount in array:
            if amount >= largest_amount:
                largest_amount = amount
        return print(largest_amount)

obj = Solution()
obj.maximum_wealth( [[1,2,3],[3,2,1]])
