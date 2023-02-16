from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows_max = len(mat)
        cols_max = len(mat[0])
        def zeroPopulate():
            ans = [[-1 for i in range(cols_max)] for j in range(rows_max)]
            ansQ = deque()
            for i in range(rows_max):
                for j in range(cols_max):
                    if(mat[i][j] == 0):
                        ans[i][j] = 0
                        ansQ.append([i,j])
            
            while(ansQ):
                el = ansQ.popleft()
                row_c = el[0]
                col_c = el[1]
                print(row_c,col_c)

                if(row_c - 1 >= 0  and mat[row_c - 1][col_c] == 1):
                    ansAssigned = ans[row_c - 1][col_c]
                    if(ansAssigned == -1 or ansAssigned > (ans[row_c][col_c] + 1)):
                        ans[row_c - 1][col_c] = ans[row_c][col_c] + 1
                        ansQ.append([row_c - 1, col_c])
                if(row_c + 1 <= rows_max -1 and mat[row_c + 1][col_c] == 1):
                    ansAssigned = ans[row_c + 1][col_c]
                    if(ansAssigned == -1 or ansAssigned > (ans[row_c][col_c] + 1)):
                        ans[row_c + 1][col_c] = ans[row_c][col_c] + 1
                        ansQ.append([row_c + 1, col_c])
                if(col_c - 1 >= 0 and mat[row_c][col_c - 1] == 1):
                    ansAssigned = ans[row_c][col_c - 1]
                    if(ansAssigned == -1 or ansAssigned > (ans[row_c][col_c] + 1)):
                        ans[row_c ][col_c- 1] = ans[row_c][col_c] + 1
                        ansQ.append([row_c, col_c - 1])
                
                if(col_c + 1 <= cols_max -1 and mat[row_c][col_c + 1] == 1):
                    
                    ansAssigned = ans[row_c][col_c + 1]
                    # print("Checking ",row_c,col_c + 1,col_c + 1 <= cols_max -1 ,mat[row_c][col_c + 1] == 1, ansAssigned == -1, ansAssigned > (ans[row_c][col_c] + 1), ansAssigned)
                    if(ansAssigned == -1 or ansAssigned > (ans[row_c][col_c] + 1)):
                        ans[row_c][col_c + 1] = ans[row_c][col_c] + 1
                        ansQ.append([row_c, col_c + 1])
            return ans
        return zeroPopulate()


        
            
        
        def nearest0():
            def helper(row, col):
                if(mat[row][col] == 0):
                    return 0
                if(ans[row][col] != -1):
                    return ans[row][col]
                visited = [[0 for i in range(cols_max)] for j in range(rows_max)]
                queue = deque()
                queue.append([row, col, 0])
                while(queue):
                    el = queue.popleft()
                    row_c = el[0]
                    col_c = el[1]
                    len_c = el[2]
                    visited[row_c][col_c] = 1
                    if(mat[row_c][col_c] == 0):
                        return len_c
                    if(row_c - 1 >= 0  and visited[row_c - 1][col_c] == 0):
                        queue.append([row_c-1, col_c, len_c + 1])
                    if(row_c + 1 <= rows_max -1 and visited[row_c + 1][col_c] == 0):
                        queue.append([row_c +1, col_c, len_c + 1])
                    if(col_c - 1 >= 0 and visited[row_c][col_c - 1] == 0):
                        queue.append([row_c, col_c - 1, len_c + 1])
                    if(col_c + 1 <= cols_max -1) and visited[row_c][col_c + 1] == 0:
                        queue.append([row_c, col_c+ 1, len_c + 1])   
            #search for a 0
            ans = [[-1 for i in range(cols_max)] for j in range(rows_max)]
            for i in range(rows_max):
                for j in range(cols_max):
                    ans[i][j] = helper(i,j)     
            return ans
