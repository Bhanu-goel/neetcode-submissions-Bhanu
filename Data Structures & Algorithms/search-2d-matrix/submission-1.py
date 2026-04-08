class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        totalrows = len(matrix)
        totalcols = len(matrix[0])

        top = 0
        bot = totalrows-1
        while(top <= bot):
            row = top + (bot-top)//2
            if target > matrix[row][-1]:
                top = row+1
            elif target < matrix[row][0]:
                bot = row-1
            else:
                break
        
        if not (top <= bot):
            return False
        
        row = top + (bot-top)//2
        l,r = 0,totalcols-1
        while l<=r:
            m = l + (r-l)//2
            if target == matrix[row][m]:
                return True
            elif target > matrix[row][m]:
                l = m+1
            else:
                r = m-1
        return False