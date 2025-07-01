#
# @lc app=leetcode.cn id=54 lang=python3
# @lcpr version=30201
#
# [54] 螺旋矩阵
#

# @lc code=start
from typing import List
class Solution:
    """主要思路是：设置left_bound,right_bound,up_bound,lower_bound四个边界，
    然后从左到右，从上到下，从右到左，从下到上，依次遍历矩阵，
    每次遍历完后更新边界。直到到边界时结束遍历。"""
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:    
        n = len(matrix)
        m = len(matrix[0])
        left_bound, right_bound = 0, m - 1
        up_bound, lower_bound = 0, n - 1

        res = []
        #创建的列表，存放结果

        while left_bound <= right_bound:
            #遍历的规则里面
            #i是行 j是列
            #从左往右遍历
            #遍历 最上面的一行，然后塞入 res

            for j in range(left_bound, right_bound + 1):
                res.append(matrix[up_bound][j])
            up_bound += 1
            #更新了上边界

            for i in range(up_bound, lower_bound + 1):
                #从上往下遍历
                #遍历 右边这一列，并且塞入 res 
                res.append(matrix[i][right_bound])
                #i是按行来走动的。列是不变的。
                right_bound -= 1
            
            for j in range(right_bound, left_bound -1, -1):
                #从右往左遍历
                #遍历最下面的一行，并且塞入 res
                #j是按列来走动的。行是不变的。所以行这是 lower_bound
                res.append(matrix[lower_bound][j])
                lower_bound -= 1
                #lower向上走

            for i in range(lower_bound, up_bound - 1, -1):
                #从下往上遍历
                res.append(matrix[i][left_bound])
                #i是按行来走动的。列是不变的。所以列这是 left_bound
                left_bound += 1
                #left向右走
        return res
# @lc code=end



#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3,4],[5,6,7,8],[9,10,11,12]]\n
# @lcpr case=end
#

