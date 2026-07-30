class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # floyd环
        # 快指针每次走2步，慢指针每次走1步
        # 相遇的位置停下
        # 快指针回到0，快慢指针每次走一步，相遇的位置就是重复的数
        slow = fast = 0 # 从0开始，因为值域在[1, n]，第一个数永远不会入环
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break
        fast = 0 # 需要回到下标0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow