class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2147483648   # -2^31
        MAX = 2147483647    # 2^31 - 1
        sign = 1    # can also use boolean

        if x < 0:
            sign = -1
            x = -x

        res = 0
        while x > 0:
            digit = x % 10
            x = x // 10

            if res > MAX // 10:   # overflow after multiplying by 10
                return 0
            if res == MAX // 10 and digit > MAX % 10:   # last digit exceeds limit
                return 0
                
            res = res * 10 + digit
        return res * sign