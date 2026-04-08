class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            l = i+1
            r = len(nums)-1

            if (i > 0) and nums[i] == nums[i-1]:
                continue
            while l<r:
                if (nums[i] + nums[l] + nums[r]) == 0:
                    result.add((nums[i],nums[l],nums[r]))
                    l+=1
                    r-=1
                elif (nums[i] + nums[l] + nums[r]) < 0:
                    l+=1
                else:
                    r-=1
        return list(result)
