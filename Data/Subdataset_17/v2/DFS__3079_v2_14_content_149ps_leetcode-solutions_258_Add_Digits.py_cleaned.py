class Solution:
    def addDigits(self, num: int) -> int:
        temp = num
        while temp >= 10:
            next_temp = 0
            while temp > 0:
                next_temp += temp % 10
                temp
            temp = next_temp
        return temp
solution = Solution()
print(solution.addDigits(38))
print(solution.addDigits(123))
print(solution.addDigits(0))
