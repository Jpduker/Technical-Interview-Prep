def deleteNode(self, node):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    next_temp = node.next
    node.val = node.next.val
    node.next=next_temp.next
    next_temp.next= None
    del(next_temp)
    
""" 
Algorithm
By analyzing the above two key observations, we can derive the following algorithm,

Store the next node in a temporary variable.

Copy data of the next node to the current node.

Change the next pointer of the current node to the next pointer of the next node.




"""