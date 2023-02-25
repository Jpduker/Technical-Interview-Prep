# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        oldCopy={None : None}
        
        curr = head 
        while curr:
            copy = Node(curr.val)
            oldCopy[curr] = copy
            curr=curr.next
            
        curr = head 
        while curr:
            copy = oldCopy[curr]
            copy.next = oldCopy[curr.next]
            copy.random = oldCopy[curr.random]
            curr = curr.next
        return oldCopy[head]


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

# Set the next pointers
node1.next = node2
node2.next = node3
node3.next = node4

# Set the random pointers
node1.random = node3
node2.random = node4
node3.random = node1
node4.random = node2

head = node1

s = Solution()
print(s.copyRandomList(head))