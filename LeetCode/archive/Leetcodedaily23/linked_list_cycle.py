# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        while slow and fast:
            slow = slow.next
            fast = fast.next
            if fast != None and fast.next != None:
                fast = fast.next
            else:
                return False
            
            if slow != None and fast != None and slow == fast:
                return True
        return False

        
