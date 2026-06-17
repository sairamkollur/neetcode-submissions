import heapq

class Solution:  # Fixed: Added missing colon
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Implement a max-heap by inverting values
        negativeHeap = [-x for x in stones]

        heapq.heapify(negativeHeap)

        while len(negativeHeap) > 1:
            # Fixed: Prefixed heap operations with 'heapq.' module namespace
            largest = -1 * heapq.heappop(negativeHeap)
            largest2 = -1 * heapq.heappop(negativeHeap)

            # If they are not equal, a new stone of weight (largest - largest2) is formed
            if largest != largest2:
                heapq.heappush(negativeHeap, -1 * (largest - largest2))
        
        return -1 * negativeHeap[0] if negativeHeap else 0