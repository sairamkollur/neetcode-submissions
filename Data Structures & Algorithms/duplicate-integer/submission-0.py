class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # return len(set(nums)) != len(nums)
        duplicate = set()

        for num in nums:
            if num in duplicate:
                return True
            duplicate.add(num)

        return False