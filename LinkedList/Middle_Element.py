from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(arr):
    dummy = ListNode()
    current = dummy

    for num in arr:
        current.next = ListNode(num)
        current = current.next

    return dummy.next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head

        if head.next == None:
            return head 
            
        while fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        
        while fast.next != None:
            slow = slow.next
        
        return slow

s = Solution()

head = create_linked_list([1, 2, 3])
print(s.middleNode(head))      # 2

head = create_linked_list([1, 2, 3, 4])
print(s.middleNode(head))      # 3

head = create_linked_list([1])
print(s.middleNode(head))      # 1