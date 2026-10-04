class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            num = self.sum_of_digits(num)
        return num
    def sum_of_digits(self, num: int) -> int:
        total = 0
        while num > 0:
            total += num % 10
            num
        return total
solution = Solution()
print(solution.addDigits(38))
print(solution.addDigits(123))
print(solution.addDigits(0))
