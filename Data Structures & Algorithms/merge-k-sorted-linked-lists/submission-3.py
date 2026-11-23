# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
# 
class Solution: 
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        heap = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        while heap:
            value, i, node = heapq.heappop(heap)
            tail.next = node

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
            
            tail = tail.next

        return dummy.next

        

        

    