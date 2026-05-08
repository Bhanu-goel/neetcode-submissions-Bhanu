import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for i in points:
            x,y = i
            dist = (x)**2+(y)**2
            heapq.heappush(heap,(dist,i))
        
        ans = []
        while k:
            dist,points = heapq.heappop(heap)
            ans.append(points)
            k-=1
        
        return ans
