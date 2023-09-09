#https://leetcode.com/problems/split-linked-list-in-parts/description/?envType=daily-question&envId=2023-09-06
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getListLen(self, head :  Optional[ListNode]):
        copy_head = head
        if copy_head == None:
            return 0
        count = 0
        while copy_head:
            count = count + 1
            copy_head = copy_head.next
        return count


    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        listLen = self.getListLen(head)
        # print("Listlen : ", listLen)

        if listLen % k != 0:
            max_els = int(listLen/k) + 1 #number of elements in eac
            limit_rows_1 = k * max_els - listLen
            limit_rows = k - limit_rows_1
        else:
            max_els = int(listLen/k)
            limit_rows = k
            limit_rows_1 = 0



        
        res = []

        new_head = None
        el_count = 0
        node_count = 0
        while head:
            # print("Processing ", head.val)
            if not new_head:
                new_head = head
                # print("Set new head  ", new_head.val)
            el_count +=1 
            # print("El count   ", el_count)
            if el_count == max_els:
                # print("El count lim ", max_els)
                prev = head
                head = head.next
                prev.next = None
                res.append(new_head)
                node_count +=1 
                el_count = 0
                if node_count == limit_rows:
                    max_els = max_els -1
                new_head = None
            else:
                head = head.next


        while node_count < k:
            res.append(None)
            node_count += 1
        return res


        
