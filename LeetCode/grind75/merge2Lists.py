# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if(list1 == None and list2== None):
            return None
        
        if(list1 == None):
            return list2

        if(list2 == None):
            return list1
        

        if list1.val <= list2.val:
            current = list1
            list1 = list1.next
        else:
            current = list2
            list2 = list2.next

        start = current

        while(current != None and list1 != None and list2 != None):
            nextNode = None
            if list1.val <= list2.val:
                nextNode = list1
                list1 = list1.next
            else:
                nextNode = list2
                list2 = list2.next
        
            current.next = nextNode
            current = current.next
        

        if(list1 != None and list2 == None):
            current.next = list1
        
        if(list2 != None and list1 == None):
            current.next = list2
        

        return start



