class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        leftptr = 1

        for rightptr in range(1, len(nums)):
            if nums[rightptr] != nums[rightptr-1]:
                nums[leftptr] = nums[rightptr]
                leftptr += 1
        return leftptr
        