class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1hash = [0] * 26
        s2hash = [0] * 26

        s1len = len(s1)
        s2len = len(s2)

        if s1len > s2len:
            return False

        left = 0
        right = 0

        while right < s1len:
            s1hash[ord(s1[right]) - ord('a')] += 1
            s2hash[ord(s2[right]) - ord('a')] += 1
            right += 1

        right -= 1

        while right < s2len:
            if s1hash == s2hash:
                return True

            right += 1

            if right != s2len:
                s2hash[ord(s2[right]) - ord('a')] += 1
            s2hash[ord(s2[left]) - ord('a')] -= 1
            left += 1

        return False