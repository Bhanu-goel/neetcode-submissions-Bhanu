def count(num):
    num &= 0xFFFFFFFF
    bits = [0]*32
    for i in range(32):
        bits[i] = num&1
        num >>= 1
    return bits[::-1]

class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        res = 0
        abits = count(a)
        bbits = count(b)
        # print(abits)
        # print(bbits)
        for i in range(31,-1,-1):
            sum_bit = abits[i] ^ bbits[i] ^ carry
            carry = (abits[i] & bbits[i]) | (carry & (abits[i] ^ bbits[i]))
            res += sum_bit*(2**(31-i))
        
        if res >= 2**31:
            res -= 2**32

        return res