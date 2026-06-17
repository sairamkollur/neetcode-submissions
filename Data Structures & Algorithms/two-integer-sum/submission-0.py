class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            val = target - nums[i]
            if val in d.keys():
                return [d[val],i]
            d[nums[i]] = i # purpose is dict is emty and cause of hashing we Store the current number and its index
        