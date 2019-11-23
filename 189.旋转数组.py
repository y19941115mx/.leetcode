#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#
# https://leetcode-cn.com/problems/rotate-array/description/
#
# algorithms
# Easy (39.39%)
# Likes:    417
# Dislikes: 0
# Total Accepted:    79.6K
# Total Submissions: 202.1K
# Testcase Example:  '[1,2,3,4,5,6,7]\n3'
#
# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
#
# 示例 1:
#
# 输入: [1,2,3,4,5,6,7] 和 k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
# 向右旋转 2 步: [6,7,1,2,3,4,5]
# 向右旋转 3 步: [5,6,7,1,2,3,4]
#
#
# 示例 2:
#
# 输入: [-1,-100,3,99] 和 k = 2
# 输出: [3,99,-1,-100]
# 解释:
# 向右旋转 1 步: [99,-1,-100,3]
# 向右旋转 2 步: [3,99,-1,-100]
#
# 说明:
#
#
# 尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
# 要求使用空间复杂度为 O(1) 的 原地 算法。
#
#
#
from typing import List

# @lc code=start


class Solution:
    # 暴力解法 按照提示每次将整个数组后移一个元素 答案是对的，但是频繁的交换操作对性能的损耗过大，导致执行时间过长，没有ac
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)

        for i in range(k):
            self.backward_one_item(nums)
        print(nums)

    def backward_one_item(self, nums: List[int]) -> None:
        list_length = len(nums)
        temp = nums[list_length - 1]

        for index in range(list_length):
            nums[index], temp = temp, nums[index]


# @lc code=end

# @lc code=start

class Solution2:
    # 使用list数据结构自带的api完成
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)

        for i in range(k):
            nums.insert(0, nums.pop())

# @lc code=end

class Solution3:
    # 使用官方题解
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)
    
    def reverse(self, nums:List[int], start:int , end:int) -> None:
        mid = (end - start) // 2
        for index in range(mid + 1):
            nums[start + index], nums[end - index] = nums[end - index], nums[start + index]


    
