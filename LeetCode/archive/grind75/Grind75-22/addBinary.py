#https://leetcode.com/problems/add-binary/
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        listA = list(a)[::-1]
        nA = len(listA)
        listB = list(b)[::-1]
        nB = len(listB)
        finList = []
        
        if(nA > nB):
            #nB needs the extra 0s
            for i in range(nA - nB):
                listB.append('0')
            nB = nA
        else:
            for i in range(nB - nA):
                listA.append('0')
            nA = nB
        
                
        
        
        # print("A", listA)
        # print("B", listB)
        i = 0
        carry = 0
        while(i < nA):
            numA = int(listA[i])
            numB = int(listB[i])
            valI = numA + numB + carry
            carry = valI //2
            valI = valI % 2
            # print("On adding ", numA, numB, " count ", valI, " carry ", carry)
            finList.append(str(valI))
            i+=1
        if(carry != 0):
            finList.append(str(carry))
        
        
        
        return ''.join(finList[::-1])
            
            
        
        
        
        
