class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initialize two pointers: one at the start, one at the end
        l, r = 0, len(s) - 1

        while l < r:
            # Move the left pointer forward if the character is not alphanumeric
            while l < r and not self.alphaNum(s[l]):
                l += 1
            # Move the right pointer backward if the character is not alphanumeric
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            
            # Compare characters (case-insensitive)
            if s[l].lower() != s[r].lower():
                return False
            
            # Move both pointers inward
            l, r = l + 1, r - 1
            
        return True

    def alphaNum(self, c):
        # Custom helper to check if a character is alphanumeric using ASCII values
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))