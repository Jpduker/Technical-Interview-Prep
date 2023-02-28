class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists):
        if not lists or len(lists) ==0:
            return None
        
        #Loop untill the lists is having only one list which is the required merged list.
        
        while(len(lists)>1):
            mergedLists = []
            
            for i in range(0,len(lists),2):
                l1= lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                
                mergedLists.append(self.mergeList(l1,l2))
            lists = mergedLists
            
        return lists[0]
        
        
        
        
    def mergeList(self,l1,l2):
        dummy = ListNode()
        tail = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next
    
"""
Approach for this problem:
consider we have 4 sorted lists, we can sort them by following 
then merge the 

step1: initially merge two of them using an helper function which is 
       nothing but the code used for merge 2 sorted arrays and make it as single list.
step2: continue the process for the remaining two lists and make it into a single list
step3: after these steps we will have totally 2 lists, we can again merge them into a single
       list which is our required list
"""