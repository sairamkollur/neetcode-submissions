class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        
        # 1. Save the last 'k' elements into a temporary list
        temp = nums[n-k:]
        
        # 2. Shift the remaining elements to the right by 'k' steps
        # We must loop backwards so we don't overwrite numbers we haven't moved yet!
        for i in range(n - k - 1, -1, -1):
            nums[i + k] = nums[i]
            
        # 3. Paste the saved temporary elements into the front of the array
        for i in range(k):
            nums[i] = temp[i]