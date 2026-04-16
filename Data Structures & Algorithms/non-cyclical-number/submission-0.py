def dig(num):
    lst = []
    while num>0:
        mod = num%10
        lst.append(mod**2)
        num//=10
    return lst

class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while True:
            s.add(n)
            digits = dig(n)
            total = sum(digits)
            if total == 1:
                return True
            if total in s:
                break
            n = total
        return False