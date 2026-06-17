class Solution:
    def mySqrt(self, x: int) -> int:
        # using binary search O(log n)
        
        left , right = 0 , x
        result = x
        
        while left <= right:
            middle = (left + right) // 2
            if middle**2 > x:
                right = middle - 1
            elif middle**2 < x:
                left = middle + 1
                result = middle # greatest mid value we can square
                
            else:
                return middle
        return result