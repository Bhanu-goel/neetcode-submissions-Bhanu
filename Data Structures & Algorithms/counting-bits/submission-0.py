def count(n):
    cnt = 0
    while n>0:
        n = n & n-1
        cnt += 1
    return cnt

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            ans.append(count(i))
        return ans