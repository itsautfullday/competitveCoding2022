#https://leetcode.com/problems/string-compression/editorial/
class Solution:
    def compress(self, chars: List[str]) -> int:
        final_count = 0
        group_count = 0
        n = len(chars)
        for i in range(n):
            char_i = chars[i]
            char_behind = None if i == 0 else chars[i-1]
            print(char_i, i, group_count, char_behind)
            if char_behind == None or char_behind !=  char_i:
                #In this case this a new group 
                group_count = 1
                final_count +=1
                chars[final_count - 1] = char_i
            else:
                #char behind is not none and char_behind == char_i
                group_count +=1
                if group_count == 2:
                    final_count += 1
                    chars[final_count - 1] = str(group_count)
                if group_count > 2 and group_count < 10:
                    chars[final_count - 1] = str(group_count)
                elif group_count >= 10 and group_count < 100:
                    final_count +=1
                    chars[final_count-2], chars[final_count - 1] = str(group_count).split('')
                elif group_count >= 100 and group_count < 10000:
                    final_count +=1
                    chars[final_count-3],chars[final_count-2], chars[final_count - 1] = str(group_count).split('')
                elif group_count >= 1000:
                    final_count +=1
                    chars[final_count-4],chars[final_count-3],chars[final_count-2], chars[final_count - 1] = str(group_count).split('')        
        print(final_count)
        return final_count
                



        
