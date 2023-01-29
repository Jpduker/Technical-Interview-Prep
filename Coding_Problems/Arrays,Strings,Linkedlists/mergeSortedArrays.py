def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    #keep track of head and tail node to add elements one after other iteratively
    head = ListNode()
    tail = head
    
    #Iterate throught both the list and add smallest to tail.next and update tail
    while(list1 !=None and list2 !=None):
        if list1.val < list2.val:
            tail.next = list1
            list1=list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail =tail.next
    if list1 == None:
        tail.next= list2
    if list2==None:
        tail.next= list1
    
    return head.next