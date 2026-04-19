class Solution:
    def reverseBits(self, n: int) -> int:
        bits = [0]*32
        for i in range(32):
            if n&1:
                bits[i] = 1
            n = n>>1
        ans = 0
        for i in range(31,-1,-1):
            ans = ans + (2**i)*bits[31-i]
        return ans