# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
# We need a loop that we can use to gather the index and value of each list and push into the heap. So 2 loops, 1st loop will push the elements into the heap, second will loop until heap is done and that will be the merging the lists.
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
            


    