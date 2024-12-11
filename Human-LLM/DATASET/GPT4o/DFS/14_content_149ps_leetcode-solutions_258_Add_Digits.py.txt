class Solution:
    def addDigits(self, num: int) -> int:
        temp = num
        while temp//10 > 0 :
            temp = (temp//10)+(temp%10)
        return temp
