#https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charOccurence = {}
        n = len(s)
        
        start = 0
        end = 0
        maxLen = 0
        while(end < n):
            character = s[end]
            if(character not in charOccurence):
                charOccurence[character] = 0
            charOccurence[character] +=1
            
            # print("Addding/incrementing char ",character, charOccurence)
            
            
            if(charOccurence[character] > 1):
                #contract the sliding windown from the left
                #We have to contract to the point that we reach the character that is currently at end is removed from current winow
                runLoop = True
                while(runLoop):
                    charAtStart = s[start]
                    if(character == charAtStart):
                        runLoop = False
                    charOccurence[charAtStart] -=1
                    start +=1 
                    
                
            
            
            #whatever the state of start and end rn is, it is a substring with unique chars, hence eligible of checking against maxLen
            maxLen = max(maxLen, (end - start + 1))
            end +=1
        
        
        
        return maxLen
    
    
    def lengthOfLongestSubstringOptimised(self, s:str) -> int:
        
        charLastOccured = {}
        n = len(s)
        
        start = 0 
        end = 0
        maxLen = 0
        
        while(end < n):
            character = s[end]
            # print("Start ",start, " End ",end, s[start : end + 1], character, (character in charLastOccured))
            
            if(character in charLastOccured and (start <= charLastOccured[character] and charLastOccured[character] <= end)):
                #Need to contract the sliding window to  charLastOccured[character] + 1
                start = charLastOccured[character] + 1
            
            #now start and end are in a space of s[start...end] is unique
            
            maxLen = max(maxLen, end - start + 1)
            charLastOccured[character] = end
            end +=1
            
        return maxLen
                
                
                
                
                
        
