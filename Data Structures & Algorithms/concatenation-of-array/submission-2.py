
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # ans = nums +nums
        # return ans

        n = len(nums)
        ans = [0]*(2*n)

        for i,num in enumerate(nums):
            ans[i] = num
            ans[i+n] = num

        return ans
    
# used range(nums) but require to look into nums[i] so used enumerate(nums) 
# to get both index and value of nums. and less storage
