def removeNthFromEnd(self, head: Optional n: int) -> Optional[ListNode]:
    
    #[1,2,3,4,5]
    
    #Find the length of the list
    length=0
    curr =head
    
    while curr:
        curr = curr.next
        length+=1
    #When we wnat to remove the first node there is not prev node hence we can just return head.next
    if length ==n:
        return head.next
    #find the node before to the node we want to delete and update its next pointer to next node's next
    node_before = length - n -1
    curr = head
    
    for i in range(0,node_before):
        curr =curr.next
    curr.next = curr.next.next
    
    return head