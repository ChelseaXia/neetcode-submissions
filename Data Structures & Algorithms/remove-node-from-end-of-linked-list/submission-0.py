# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 找倒数第n个节点，考虑使用快慢指针
        # 快指针先往前走n+1步，这样两个就隔了n
        # 同时走，等fast is None的时候slow的下一个就是待删节点
        start = ListNode()
        start.next = head
        slow, fast = start, start
        for _ in range(n+1):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return start.next
        