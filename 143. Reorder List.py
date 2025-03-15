class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        backPtr, frontPtr = head, head
        while frontPtr and frontPtr.next:
            backPtr = backPtr.next
            frontPtr = frontPtr.next.next

        previousNode, currentNode = None, backPtr
        while currentNode:
            nxt = currentNode.next
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = nxt

        partOne, partTwo = head, previousNode
        while partTwo and partTwo.next:
            x = partOne.next
            y = partTwo.next

            partOne.next = partTwo
            partTwo.next = x

            partOne = x
            partTwo = y