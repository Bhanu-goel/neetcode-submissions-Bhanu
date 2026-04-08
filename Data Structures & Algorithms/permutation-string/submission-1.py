class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        windowsize = len(s1)
        l=0
        s1freq = {}
        for i in s1:
            s1freq[i] = s1freq.get(i,0)+1

        while l<(len(s2)-windowsize+1):
            s2freq = {}
            substring = s2[l:l+windowsize]
            for i in substring:
                s2freq[i] = s2freq.get(i,0)+1
            print(s1freq,s2freq)
            if s1freq == s2freq:
                return True
            l+=1
        return False