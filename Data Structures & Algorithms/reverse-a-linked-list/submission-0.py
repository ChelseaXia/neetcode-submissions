# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        pre = None
        while cur: # 循环停止条件，一定要把最后一个节点也处理完
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node
        return pre # 返回的是前面的那个节点