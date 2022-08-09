#https://leetcode.com/problems/implement-trie-prefix-tree/
class Node:
        _linkages = {}
        val = ""
        isEnd = False
        
        def __init__(self, char = ""):
            self.val = char
            self.isEnd = False
            self._linkages = {}
        
        def setIsEnd(self, val):
            self.isEnd = val
        
        def isNodeInLinkages(self, val):
            # print("Checking value of ", val," in node of val ", self.val, self._linkages.keys() ,(val in self._linkages))
            return val in self._linkages
        
        def getNodeValue(self,val):
            return self._linkages[val]
        
        def addNodeToLinkages(self, node):
            # print("Adding node ", node.val, " to ", self.val)
            self._linkages[node.val] = node
            
            

class Trie:
    def __init__(self):
        self.root =  Node()

    def insert(self, word: str) -> None:
        node = self.root
        # print("Node value is ", node)
        for char in word:
            if(node.isNodeInLinkages(char)):
                node = node.getNodeValue(char)
                # print("Node value is ", node)
            else:
                newNode =  Node(char)
                node.addNodeToLinkages(newNode)
                node = node.getNodeValue(char)
                # print("Node value is ", node)
        node.setIsEnd(True)
        

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if(node.isNodeInLinkages(char)):
                node = node.getNodeValue(char)
            else:
                return False
        return node.isEnd
            

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if(node.isNodeInLinkages(char)):
                node = node.getNodeValue(char)
            else:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
