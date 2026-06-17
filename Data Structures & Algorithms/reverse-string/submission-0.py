class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Set our two pointers at the very beginning and very end of the list
        left = 0
        right = len(s) - 1
        
        # Loop until the two pointers meet in the middle
        while left < right:
            # Swap the characters at the left and right pointers
            s[left], s[right] = s[right], s[left]
            
            # Move the pointers closer to the center
            left += 1
            right -= 1