
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        mp = {}

        for num in nums2:

            while stack and num > stack[-1]:
                smaller = stack.pop()
                mp[smaller] = num

            stack.append(num)

        ans = []

        for num in nums1:
            ans.append(mp.get(num, -1))

        return ans
