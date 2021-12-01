"""
NOTE: This is hellaciously slow and could be done much better.
"""

class Node:
    def __init__(self, val=0, nxt=None, prev=None):
        self.val = val
        self.nxt = nxt
        self.prev = prev

class MinStack:

    def __init__(self):
        self.head = Node(val=sys.maxsize)
        self.min = sys.maxsize

    def push(self, val: int) -> None:
        node = Node(val, prev=self.head)
        self.head.nxt = node
        self.head = node
        self.min = min(self.min, val)

    def pop(self) -> None:
        self.head = self.head.prev
        self.head.nxt = None
        cur = self.head
        newMin = self.head.val
        
        while cur:
            newMin = min(newMin, cur.val) 
            print(cur.val)
            cur = cur.prev
        self.min = newMin

    def top(self) -> int:
        return self.head.val 

    def getMin(self) -> int:
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
