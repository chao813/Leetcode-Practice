"""Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
"""

def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        temp = []
        while head != None:
            temp.append(head.val)
            head = head.next
        
        return temp == temp[::-1]