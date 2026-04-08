class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        prefix = [0]*len(height)
        suffix = [0]*len(height)
        prefix[0] = height[0]
        suffix[len(height)-1] = height[len(height)-1]

        for i in range(1,len(height)):
            prefix[i] = max(prefix[i-1],height[i])

        for i in range(len(height)-2,-1,-1):
            suffix[i] = max(suffix[i+1],height[i])

        for i in range(len(height)):
            total+=abs(min(prefix[i],suffix[i])-height[i])
            
        return total