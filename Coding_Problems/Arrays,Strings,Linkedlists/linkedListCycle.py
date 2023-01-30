def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head==None or head.next==None:
            return False
        hashmap={}
    
        while head is not None:
            if head in hashmap:
                return True
            hashmap[head]=head
            head = head.next
        return False