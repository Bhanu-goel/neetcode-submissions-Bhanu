class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x = 0
        for i in range(0,len(nums)):
            x ^= nums[i]

        return x