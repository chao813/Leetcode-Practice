"""Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3"""

def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        
        while current != None and current.next != None:
            if current.next.val == current.val:
                current.next = current.next.next;
            else:
                current = current.next
        
        return head
    