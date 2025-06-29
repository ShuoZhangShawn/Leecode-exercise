#
# @lc app=leetcode.cn id=48 lang=python3
# @lcpr version=30201
#
# [48] 旋转图像
#

# @lc code=start
import sys

def solve():
    """
    这个函数封装了解决一个测试用例的完整逻辑。
    """
    # 1. 读取输入 (Input Handling)
    try:
        # 读取第一行，获取矩阵维度 N
        # sys.stdin.readline() 会读入一行，包括末尾的换行符'\n'，所以用 .strip() 去掉
        line = sys.stdin.readline()
        if not line:  # 处理输入结束的情况
            return
        n = int(line.strip())
        
        matrix = []
        for _ in range(n):
            # 循环读取 N 行
            # .split() 会按空格分割字符串，返回一个字符串列表
            # map(int, ...) 将列表中的每个字符串转换为整数
            row = list(map(int, sys.stdin.readline().strip().split()))
            matrix.append(row)
            
    except (IOError, ValueError):
        # 捕获可能的读取错误或数据格式转换错误
        return

    # 2. 核心算法 (Core Algorithm)
    # 这里的代码和你优化后的 LeetCode 代码完全一样
    # 2.1 沿主对角线转置
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # 2.2 反转每一行
    for row in matrix:
        row.reverse()

    # 3. 格式化输出 (Output Formatting)
    for row in matrix:
        # 将行内所有整数用 map(str, ...) 转换回字符串
        # 用 " ".join(...) 将它们用空格连接成一个字符串
        print(" ".join(map(str, row)))

# 程序主入口
if __name__ == "__main__":
    # 很多 ACM 题目可能有多个测试用例，需要用 while 循环处理
    # while True:
    #     try:
    #         solve()
    #     except EOFError:
    #         break
    # 对于这道题，通常只有一个测试用例，所以直接调用一次即可。
    solve()

        
        
# @lc code=end



#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]\n
# @lcpr case=end

#

