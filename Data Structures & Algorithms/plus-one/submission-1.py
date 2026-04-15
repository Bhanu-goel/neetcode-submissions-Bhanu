def digi(num):
    ans = []
    while num>0:
        mod = num%10
        ans.append(mod)
        num//=10
    return ans[::-1]

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [str(i) for i in digits]
        num = int(''.join(digits))
        num += 1
        return digi(num)