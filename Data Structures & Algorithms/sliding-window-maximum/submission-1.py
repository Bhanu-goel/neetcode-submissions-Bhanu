class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        lst = nums[:k]
        maxi = max(lst)
        res.append(maxi)
        i=1
        while i<len(nums)-k+1:
            # lst.remove(nums[i-1])
            if nums[i-1] == maxi:
                maxi = max(nums[i:i+k])
            else:    
                if nums[i+k-1] > maxi:
                    maxi = nums[i+k-1]
            res.append(maxi)
            i+=1 
        return res