def freq(s):
        d = dict()
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i]+=1
        return d
        
class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        sdict = freq(s)
        tdict = freq(t)
        return sdict == tdict