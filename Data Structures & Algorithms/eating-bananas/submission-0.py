import math
def possible(piles,hour,k):
    h = 0
    for i in piles:
        h += math.ceil(i/k)
    return h <= hour
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 0
        r = sum(piles)
        mineat = float('infinity')
        while l<=r:
            mid = l + (r-l)//2
            if mid == 0:
                l = mid + 1
            elif possible(piles,h,mid):
                mineat = min(mineat,mid)
                r = mid - 1
            else:
                l = mid + 1
        return mineat