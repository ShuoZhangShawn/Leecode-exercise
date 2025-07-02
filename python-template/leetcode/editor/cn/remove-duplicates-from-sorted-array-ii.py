#
# @lc app=leetcode.cn id=80 lang=python3
# @lcpr version=30201
#
# [80] 删除有序数组中的重复项 II
#

# @lc code=start
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0
            return 0
        
        slow = 0
        fast = 0
        count = 0

        while fast < len(nums):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
                #遇到新值加进去

            elif count < 2 and slow < fast:
                slow += 1
                nums[slow] = nums[fast]
                #如果是旧值，计数小于2，也加进去。
            
            fast += 1
            count += 1
            if fast < len(nums) and nums[fast] != nums[slow]:
                count = 0
                #重制count
                    # 数组长度为索引 + 1
        return slow + 1

               

# @lc code=end



#
# @lcpr case=start
# [1,1,1,2,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,1,1,1,1,2,3,3]\n
# @lcpr case=end

#

