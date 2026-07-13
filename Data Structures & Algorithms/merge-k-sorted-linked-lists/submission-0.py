# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        start = ListNode()
        cur = start
        min_heap = []
        for i in range(k):
            head = lists[i]
            heapq.heappush(min_heap, (head.val, i, head))
        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            cur.next = node
            cur = cur.next
            nxt = node.next
            if nxt:
                heapq.heappush(min_heap, (nxt.val, i, nxt))
        return start.next
