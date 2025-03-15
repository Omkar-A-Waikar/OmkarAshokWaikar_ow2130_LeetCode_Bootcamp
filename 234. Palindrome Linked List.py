class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if not head or not head.next:
            return True
        
        backPtr = frontPtr = head
        while frontPtr and frontPtr.next:
            backPtr = backPtr.next
            frontPtr = frontPtr.next.next
        
        prev = None
        while backPtr:
            nxt = backPtr.next
            backPtr.next = prev
            prev = backPtr
            backPtr = nxt
        
        leftPart, rightPart = head, prev
        while rightPart:  
            if leftPart.val != rightPart.val:
                return False
            leftPart = leftPart.next
            rightPart = rightPart.next
        
        return True