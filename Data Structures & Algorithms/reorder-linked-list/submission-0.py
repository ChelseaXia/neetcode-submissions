# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 先找中点，快慢指针
        # 找到后，中点之前的为前段，中点之后的为后段，把前段和后段断开
        # 反转后段
        # 交替拼接
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        # 要断链
        slow.next = None

        # 反转
        pre = None
        cur = mid
        while cur:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node
        l1, l2 = head, pre
        while l1 and l2:
            l1_next = l1.next
            l2_next = l2.next

            l1.next = l2
            # 如果l1已经走完了，就结束
            if l1_next is None:
                break
            l2.next = l1_next
            l1 = l1_next
            l2 = l2_next