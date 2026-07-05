class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = defaultdict(int)
        res = 0

        # if each char count becomes even, add 2
        for char in s:
            count[char] += 1
            if count[char] % 2 == 0:
                res += 2

        # using hash map values
        # add one odd char in center
        for cunt in count.values():
            if cunt % 2:
                res += 1
                break

        # returns answer
        return res