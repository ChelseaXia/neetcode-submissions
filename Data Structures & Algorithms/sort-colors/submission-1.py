class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 看到什么想到什么：三指针（l, i, b）原地分区，把 0 换到左边，2 换到右边
        # 边界条件：从右边换来的数可能还是 2，需要继续处理（i 不动）；从左边换来的一定已处理过（i++）。
        # r指向0的最右边，b指向2的最左边
        n = len(nums)
        r, b = 0, n-1
        i = 0
        while i<n and r <= i <= b:
            if nums[i] == 0:
                nums[r], nums[i] = nums[i], nums[r]
                r += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                nums[i], nums[b] = nums[b], nums[i]
                b -= 1
        

