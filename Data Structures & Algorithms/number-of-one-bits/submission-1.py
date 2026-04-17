class Solution:
    def hammingWeight(self, n: int) -> int:
        if n == 0:
            return 0
        cnt = 0
        while n>0:
            if n&1:
                cnt+=1
            n>>=1
        return cnt