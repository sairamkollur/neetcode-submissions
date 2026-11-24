class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen_nums = set()

        for num in nums:
            if num in seen_nums:
                return num
            seen_nums.add(num)
        return -1