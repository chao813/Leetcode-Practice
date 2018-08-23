"""Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""


def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        
        dummy = ListNode(-1)
        dummy.next = head
        current = dummy
    
        
        while current != None and current.next != None:
            if current.next.val == val:
                current.next = current.next.next;
            else:
                current = current.next
        
        return dummy.next