# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # 这个时候可以知道slow一定指向中间那个（或者两个中的后一个）
        # 反转后面的链表
        def reverse(node):
            cur = node
            pre = None # 这里注意必须要是None不能是ListNode(0)
            while cur:
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            return pre
        # 进行一个比较
        p2 = reverse(slow)
        p1 = head
        while p2:
            if p2.val != p1.val:
                return False
            p2 = p2.next
            p1 = p1.next
        return True

