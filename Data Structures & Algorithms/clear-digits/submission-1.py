
class Solution:
    def clearDigits(self, s: str) -> str:

        res = ""

        for char in s:

            if char.isdigit():
                res = res[:-1]

            else:
                res += char

        return res
