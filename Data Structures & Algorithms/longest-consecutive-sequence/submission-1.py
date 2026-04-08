def checkseq(x,nums):
    c=1
    while(True):
        if (x+1) in nums:
            x+=1
            c+=1
        else:    
            break
    return c

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxcount = 0
        for i in nums:
            count = checkseq(i,nums)
            if maxcount < count:
                maxcount = count 
        return maxcount
