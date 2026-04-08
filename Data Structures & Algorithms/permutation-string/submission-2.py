class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        windowsize = len(s1)
        l=1
        s1freq = {}
        for i in s1:
            s1freq[i] = s1freq.get(i,0)+1
        s2freq = {}
        for i in s2[:windowsize]:
            s2freq[i] = s2freq.get(i,0)+1
        print(s1freq,s2freq)
        if s1freq == s2freq:
            return True
        while l<(len(s2)-windowsize+1):
            s2freq[s2[l-1]] -= 1
            if s2freq[s2[l-1]] == 0:
                del s2freq[s2[l-1]]
            print(s2[l+windowsize-1])
            s2freq[s2[l+windowsize-1]] = s2freq.get(s2[l+windowsize-1],0)+1
            print(s1freq,s2freq)
            if s1freq == s2freq:
                return True
            l+=1
        return False