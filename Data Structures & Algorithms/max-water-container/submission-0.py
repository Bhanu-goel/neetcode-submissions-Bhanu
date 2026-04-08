class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxar = 0
        for i in range(len(heights)):
            width = 1
            for j in range(i+1,len(heights)):
                ar = min(heights[i],heights[j]) * width
                width+=1
                maxar = max(maxar,ar)
        return maxar