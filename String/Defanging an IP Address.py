class Solution(object):
    def defangIPaddr(self, address):
        return print(address.replace('.', '[.]'))

obj = Solution()
obj.defangIPaddr("1.1.1.1")