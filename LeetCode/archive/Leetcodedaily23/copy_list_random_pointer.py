#https://leetcode.com/problems/copy-list-with-random-pointer/
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        
        old_head = head
        ref_copy = {}
        copy_head = Node(head.val, None, head.random)
        ref_copy[head] = copy_head

        last_ref = copy_head
        head = head.next

        while head:
            copy = Node(head.val, None, head.random)
            # print("Copying ", head.val, copy.val)
            ref_copy[head] = copy
            last_ref.next = copy
            last_ref = copy


            head = head.next
        
        # print(old_head.val)
        point = copy_head
        while point:
            # print(point.val)
            if point.random:
                point.random = ref_copy[point.random]
            point = point.next
        
        return copy_head
