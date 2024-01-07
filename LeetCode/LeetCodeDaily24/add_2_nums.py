#https://leetcode.com/problems/add-two-numbers-ii/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def list_length(l1:ListNode):
            count = 0
            head = l1
            while(head):
                head = head.next
                count +=1
            return count

        # Learn how signatures would work in python dawg
        def compute(n1: ListNode, n2: ListNode):
            if n1 == None and n2 == None:
                return (None, 0)
            if n1 == None or n2 == None:
                print("Error : Lists should end together dipshit")
                return (None, 0)
            nextNode, carry = compute(n1.next, n2.next)
            val = n1.val + n2.val + carry

            new_carry = val//10
            node_val = val % 10

            newNode = ListNode(val=node_val, next=nextNode)
            return (newNode, new_carry)
        

        n1 = list_length(l1)
        n2 = list_length(l2)
        diff = abs(n1-n2)
        
        if n1 > n2:
            long,short = l1, l2 
        else:
            long,short = l2, l1


        if n1 != n2:
            for i in range(diff):
                new_node = ListNode(0, short)
                short = new_node
            #now short is the same length
        #now both should be same length
        new_head,carry = compute(long, short)
        if carry != 0:
            newest_head = ListNode(carry, new_head)
            return newest_head
        return new_head
