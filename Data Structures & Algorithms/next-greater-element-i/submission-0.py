
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        res = []

        for num in nums1:
            idx = nums2.index(num) 
            greater = -1

            for j in range(idx + 1, len(nums2)):
                if nums2[j] > num:
                    greater = nums2[j]
                    break
            res.append(greater)
        return res