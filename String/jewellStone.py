class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        if len(jewels) >= 1 and len(stones) <= 50:
            count = 0
            for i in jewels:
                for j in stones:
                    if i == j:
                        count +=1
            return print(count)
obj = Solution()
obj.numJewelsInStones("aA", "aAAbbbb")