class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tmp = {}
        for i in t:
            tmp[i] = tmp.get(i,0)+1
        windowsize = len(t)
        res = ""
        minlength = float('inf')
        for i in range(len(s)-windowsize+1):
            for j in range(i,len(s)):
                substring = s[i:j+1]
                tmp1 = {}
                for x in substring:
                    tmp1[x] = tmp1.get(x,0)+1
                print(substring)
                valid = True
                for key in tmp:
                    if tmp1.get(key,0) < tmp[key]:
                        valid = False
                        break
                if valid:
                    if minlength > len(substring):
                        minlength = len(substring)
                        res = substring
        return res