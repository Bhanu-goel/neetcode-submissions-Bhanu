import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums
        heapq.heapify_max(heap)
        k-=1
        while k:
            heapq.heappop_max(heap)
            k-=1
        return heapq.heappop_max(heap)