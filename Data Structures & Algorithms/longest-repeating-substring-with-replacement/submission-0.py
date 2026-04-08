class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charfreq = {}
        maxfreq = 0
        l=0
        res=0
        for r in range(len(s)):
            charfreq[s[r]] = charfreq.get(s[r],0)+1
            maxfreq = max(charfreq.values())
            while ((r-l+1)-maxfreq) > k:
                charfreq[s[l]] -= 1
                l+=1
            res = max(res,r-l+1)
        return res