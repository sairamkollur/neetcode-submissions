class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = {}
        num = 0
        for i in nums:
            count[i] = count.get(i, 0) + 1
        for key, value in count.items():
            num+=value*(value-1)/2
        return int(num)
            


        