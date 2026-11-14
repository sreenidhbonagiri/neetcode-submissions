# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # First find the middle and split the list into two. Then reverse that second list only to go from n - 1,  to n -2 , and so on. Then we need to merge both of the lists.
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return 

        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        while fast and fast.next:
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


        


        

        
        