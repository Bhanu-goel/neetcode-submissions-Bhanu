class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sm = 0
        for i in nums:
            sm += i

        return (len(nums)*(len(nums)+1)//2) - sm