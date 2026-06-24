class Solution:
    def climbStairs(self, n: int) -> int:
        # Base case: if there's only 1 step, there's only 1 way to climb it
        if n <= 1:
            return 1
            
        # We start from the bottom up, caching the last two steps
        one, two = 1, 1
        
        # Shift our window forward n - 1 times
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
            
        return one