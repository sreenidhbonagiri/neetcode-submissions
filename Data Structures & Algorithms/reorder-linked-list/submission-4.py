# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # First we need to find the middle of the list, and split them into two. Then, we can re order the second list to go from decreasing to increasing instead. Then we will merge the two linked lists accordingly.
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        previous = None
        current = second

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        first = head
        second = previous

        while second:
            next_first = first.next
            next_second = second.next

            first.next = second
            second.next = next_first

            first = next_first
            second = next_second


        
        

