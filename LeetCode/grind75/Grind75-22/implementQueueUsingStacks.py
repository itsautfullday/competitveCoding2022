#https://leetcode.com/problems/implement-queue-using-stacks/
from collections import deque

class MyQueue:

    def __init__(self):
        self.internalStack = deque()
        self.indexOfTop = -1

    def push(self, val: int) -> None:
        tempStack = deque()
        lenTemp = 0
        # print("Push : Trying to push ",val , self.internalStack, self.indexOfTop)
        
        while(self.internalStack and self.indexOfTop >= 0):
            top = self.internalStack[self.indexOfTop]
            self.internalStack.pop()
            self.indexOfTop -=1
            
            # print("Push : popped  ",top , " appending to temp ")
            tempStack.append(top)
            lenTemp +=1
        
        
        
        # print("Push : appending val ",val)
        self.internalStack.append(val)
        self.indexOfTop +=1
        
        while(lenTemp > 0):
            top = tempStack[lenTemp - 1]
            lenTemp -=1
            
            
            self.internalStack.append(top)
            # print("Push : Re appending ", top)
            self.indexOfTop +=1
        
        # print("Push : End of push ",self.internalStack)
        
        
        

    def pop(self) -> int:
        top = self.peek()
        self.internalStack.pop()
        self.indexOfTop -=1
        return top
        
        

    def peek(self) -> int:
        return self.internalStack[self.indexOfTop]
        

    def empty(self) -> bool:
        # print("Empty : ", self.indexOfTop)
        return self.indexOfTop == -1
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
