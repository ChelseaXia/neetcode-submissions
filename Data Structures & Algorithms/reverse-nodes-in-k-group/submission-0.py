# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        # 先确定是否够k个节点
        start = dummy # start是每一段的首节点的上一个节点
        while start.next:
            end = start
            for _ in range(k):
                end = end.next
                if end is None:
                    return dummy.next # 不需要进行后续操作了，直接返回结果
            nxt = end.next
            end.next = None # 断开这一段
            pre = start.next # 记录当前首节点（反转后会变成尾节点）
            start.next = self.reverse(start.next)# 反转该段链表，该段新头连上前面末端尾巴
            pre.next = nxt # 用该段尾巴连接下一段起始
            start = pre # 移动起始节点的前一个节点
            
        return dummy.next
    def reverse(self, head):
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre
        
        
            

