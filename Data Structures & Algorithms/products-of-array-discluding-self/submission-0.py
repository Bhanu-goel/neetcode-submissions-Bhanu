class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a1 = 1 
        a0 = 1
        if nums.count(0) > 1:
            return [0]*len(nums)

        if 0 in nums:
            for i in nums:
                if i != 0:
                    a0*=i
            for i in range(len(nums)):
                if nums[i] == 0:
                    nums[i] = a0
                else:
                    nums[i] = 0
        else:
            for i in nums:
                a1*=i
            for i in range(len(nums)):
                nums[i] = a1//nums[i]
        # print(a0,a1,sep=',')

        return nums