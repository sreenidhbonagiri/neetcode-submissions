# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Find the middle of the list so we know where to seperate the lists to re order them accordingly least to greatest then least to greatest so on. After finding the middle and seperating the two lists. We want to reverse the second list to go from highest to least. Now after reversing it, we need to merge our lists. 
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

        




        




        

        