
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        mp = {}

        for i in range(len(nums2)):
            greater = -1

            for j in range(i + 1, len(nums2)):
                if nums2[j] > nums2[i]:
                    greater = nums2[j]
                    break

            mp[nums2[i]] = greater

        ans = []

        for num in nums1:
            ans.append(mp[num])

        return ans
