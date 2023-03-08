class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        head1 = head

        head2 = head 

        i=0
        length =0
        maxsum =0
        #finding the length of the linked list 
        while head:
            head= head.next
            length+=1


        for i in range(0,int(length/2)):
            head2 = head2.next 

        prev =None
        head2 = head2

        #reversing the second half of the linked list 
        while head2 is not None:
            next_temp = head2.next
            head2.next = prev
            prev = head2
            head2 = next_temp

        head2 = prev

        #addig both the head pointers pointing the head of both the lists and adding it to maxsum variable if it's greater than actuall maxsum
        for i in range(0,int(length/2)):
            maxsum = max(head1.val +head2.val , maxsum)
            head1 = head1.next 
            head2 = head2.next

        return maxsum