#https://leetcode.com/problems/spiral-matrix/submissions/
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        states = [0, 1, 2, 3]
        #0 move right
        #1 move down
        #2 move left
        #3 move up
        rows = len(matrix)
        cols = len(matrix[0])
        count = rows * cols
        res = []
        elsAdded = 0
        
        
        rowInd = 0
        colInd = 0
        
        rows_min = 1
        cols_min = 0
        row_max = rows - 1
        cols_max = cols - 1
        
        stateOfTraversal = 0
        
        while(elsAdded < count):
            currentEl = matrix[rowInd][colInd]
            # print("Row ", rowInd, " col ", colInd, currentEl,stateOfTraversal,rows_min,cols_min, row_max,  cols_max  )
            # print("Row ", rowInd, " col ", colInd, currentEl,stateOfTraversal)
            res.append(currentEl)
            elsAdded +=1
            
            if(stateOfTraversal == 0):
                #check if traversal needs to change
                if(colInd == cols_max):
                    #traversal needs to change
                    stateOfTraversal = 1
                    cols_max -=1
                    rowInd +=1
                    # print("Changing traversal to ", stateOfTraversal,cols_max )
                else:
                    #traversal stays the same
                    colInd +=1
            elif(stateOfTraversal == 1):
                if(rowInd == row_max):
                    stateOfTraversal = 2
                    row_max -=1
                    colInd -=1
                    # print("Changing traversal to ", stateOfTraversal,row_max )
                else:
                    rowInd +=1
            elif(stateOfTraversal == 2):
                if(colInd == cols_min):
                    stateOfTraversal = 3
                    cols_min += 1
                    rowInd -=1
                    # print("Changing traversal to ", stateOfTraversal,cols_min )
                else:
                    colInd -=1
            elif(stateOfTraversal == 3):
                if(rowInd == rows_min):
                    stateOfTraversal = 0
                    rows_min += 1
                    colInd +=1
                    # print("Changing traversal to ", stateOfTraversal, rows_min)
                else:
                    rowInd -=1
            else:
                # print("WTF",stateOfTraversal)
                break
            
            if(rowInd >= rows or colInd >= cols):
                # print("Incorrect inc ", rowInd, colInd)
                break
            
            
            
            
        return res
                    
                    
                
                
                    
                    
            
