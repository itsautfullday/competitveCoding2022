def intToRoman(self, num: int) -> str:
        res = []
        powerOf10 = 0
        while(num != 0):
            pieceToEvaluate = int(num % 10)
            actualValueToEvalue = pieceToEvaluate * (10 ** powerOf10)
            lower = ""
            upper = ""
            reducer = ""
            resultant = ""
            if(powerOf10 == 0):
                #in this case lower value is V and upper is X
                lower = "V"
                upper = "X"
                reducer = "I"
            elif(powerOf10 == 1):
                #in this case lower value is L and upper is C
                lower = "L"
                upper = "C"
                reducer = "X"
            elif(powerOf10 == 2):
                #in this case lower value is L and upper is C
                lower = "D"
                upper = "M"
                reducer = "C"
            else:
                lower = "-1"
                upper = "-1"
                reducer = "M"
                
            if(pieceToEvaluate < 4):
                for i in range(pieceToEvaluate):
                    resultant += reducer
            elif(pieceToEvaluate == 4):
                resultant = reducer + lower
            elif(pieceToEvaluate == 5):
                resultant = lower
            elif(pieceToEvaluate > 5 and pieceToEvaluate < 9):
                resultant = lower
                for i in range(pieceToEvaluate - 5):
                    resultant += reducer
            elif(pieceToEvaluate == 9):
                resultant = reducer + upper
            print(pieceToEvaluate,actualValueToEvalue,powerOf10, lower, upper,reducer, resultant)
            res.append(resultant)
            num //= 10
            powerOf10+=1
        
        
        return "".join(res[::-1])
