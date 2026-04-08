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
        l=0
        r=len(nums)-1
        if target > nums[len(nums)-1] and target <= nums[mid-1]:
            r = mid-1
        else:
            l = mid
        # print(l,r)
        while l<=r:
            mid = l + (r - l)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid +1
            else:
                r = mid - 1 
        return -1