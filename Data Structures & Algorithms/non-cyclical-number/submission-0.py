class Solution:
    def isHappy(self, n: int) -> bool:
        for i in range(100):
            total = 0

            while n > 0:
                digit = n % 10
                total += digit * digit
                n //= 10

            n = total

            if n == 1:
                return True

        return False