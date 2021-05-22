class Solution(object):
    def fizzBuzz(self, n):

        array = []
        for num in range(1, n + 1):
            if num % 3 == 0 and num % 5 == 0:
                array.append("FizzBuzz")
            elif num % 3 == 0:
                array.append("Fizz")
            elif num % 5 == 0:
                array.append("Buzz")
            else:
                array.append(str(num))
        return print(array)

obj = Solution()
obj.fizzBuzz(5)