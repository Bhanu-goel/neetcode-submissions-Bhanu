class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while l<r:
            mid = l + (r - l)//2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        mid = l
        # if nums[mid] == target:
        #     return mid
        if mid == 0:
            l = 0
            r = len(nums) - 1
        else:
            if target > nums[len(nums)-1] and target <= nums[mid-1]:
                l = 0
                r = mid-1
            else:
                l = mid
                r = len(nums)-1
        print(l,r)
        while l<=r:
            mid = l + (r - l)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid +1
            else:
                r = mid - 1 
        return -1