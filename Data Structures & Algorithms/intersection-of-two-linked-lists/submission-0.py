# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # a和b走完各自之后走对方的节点，相等处就是链表相交处
        # A: a+c+b
        # B: b+c+a
        a = headA
        b = headB
        while a != b:
            # 注意：这里一定要让a走到None，而不是a.next走到none
            a = a.next if a is not None else headB
            b = b.next if b is not None else headA
        return a