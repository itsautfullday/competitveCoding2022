class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        max_row = len(matrix)
        max_col = len(matrix[0])
        dp = {}

        def minVal(row, col):
            if(row,col) in dp:
                return dp[(row, col)]

            if(row == max_row - 1):
                dp[(row, col)] = matrix[row][col]
                return dp[(row, col)]
            contentions = []
            contentions.append(minVal(row + 1, col))
            if(col - 1 >= 0):
                contentions.append(minVal(row + 1, col - 1))
            if(col + 1 < max_col):
                contentions.append(minVal(row + 1, col + 1))
            dp[(row, col)] = min(contentions) + matrix[row][col]
            return dp[(row, col)]
        
        min_top = [minVal(0,i) for i in range(max_col)]
        return min(min_top)