# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        carry = 0 # 表示进位，要么1要么0
        while l1 or l2 or carry: # 只要还有l1或者l2或者进位就继续
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            val = v1+v2+carry
            carry = val//10 # 新的进位
            nxt = ListNode()
            nxt.val = val%10
            cur.next = nxt
            cur = cur.next
            if l1: l1 = l1.next # 注意要判断是否有节点不然会超范围报错
            if l2: l2 = l2.next
        return dummy.next
            