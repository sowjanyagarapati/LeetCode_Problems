# Definition for singly-linked list.

'''Approach:
current pointer should be initialized to head
current.next is checked for non empty
if current.val == current.next.val, then current.next is updated to current.next.next
else, current pointer is moved to the next node

Time complexity: O(n) in the worst case, where n is the length of the input list. Each pointer moves at most n times combined, so overall linear.

Space complexity: O(1) extra space, since only a few variables are used regardless of input size.
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current.next:

            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head
        