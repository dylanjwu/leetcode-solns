# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def find_cycle(self, head):
        one_step = head
        two_step = head
        while one_step and two_step:
            
            one_step = one_step.next
            if two_step.next:
                two_step = two_step.next.next
            else:
                return None
            
            if one_step == two_step:
                return one_step
            
        return None
    
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        one = 3, 2, 0, -4, 2, 0, -4
        two = 3, 0, 2, -4`
        """
        
        cycle_node = self.find_cycle(head)
        
        if not cycle_node:
            return None
        
        else:
            start = cycle_node.next
            s = set()
            s.add(cycle_node) 
            while start != cycle_node:
                s.add(start)
                start = start.next

            curr = head
            while not curr in s:
                curr = curr.next

            return curr
