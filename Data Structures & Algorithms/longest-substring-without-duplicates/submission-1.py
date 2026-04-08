class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlength = 0
        charlen = [0]*256
        i=0
        j=0
        while j<len(s):
            print(f'{s[j]},{ord(s[j])}')
            if charlen[ord(s[j])] == 0:
                charlen[ord(s[j])] = 1 
                j+=1
                maxlength = max(maxlength,sum(charlen))
            else:
                charlen[ord(s[i])] = 0
                i+=1
        return maxlength