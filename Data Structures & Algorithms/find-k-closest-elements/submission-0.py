class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        '''
        given n sorted array
        2 integers k and x
        return k closest integer to x in array

        '''
        l, r = 0, len(arr) - k
        
        while l < r:
            m = (l + r) // 2
            if x - arr[m] > arr[m + k] - x:
                l = m + 1
            else:
                r = m
        return arr[l:l+k]