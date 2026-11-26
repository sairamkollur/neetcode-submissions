class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mi = 0

        for i in range(len(nums)):
            if mi < i:
                return False

            mi = max(mi, i + nums[i])
        
        return True