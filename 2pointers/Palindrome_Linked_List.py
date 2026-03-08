class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head.next

        while fast.next:
            if slow.val == fast.val:
                slow.next = fast.next
                fast = fast.next.next
            else:
                fast = fast.next
            slow = slow.next
        return head

s = Solution()
print(s.deleteDuplicates([1,2,3,4]))
