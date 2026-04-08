class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        totalrows = len(matrix)
        totalcols = len(matrix[0])

        l = 0
        r = totalrows*totalcols-1
        while l<=r:
            m = l + (r-l)//2
            row = m // totalcols
            col = m % totalcols
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                r = m - 1
            else:
                l = m + 1
        return False