class Solution(object):
    def kidsWithCandies(self, candies, extra_candies):
        highest = max(candies)
        array = []
        for candy in candies:
            candy += extra_candies
            if candy >= highest:
                array.append(True)
            else:
                array.append(False)
        return array


obj = Solution()
print(obj.kidsWithCandies([2, 3, 5, 1, 3], 3))
