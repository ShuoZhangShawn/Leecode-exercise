#
# @lc app=leetcode.cn id=48 lang=python3
# @lcpr version=30201
#
# [48] 旋转图像
#

# @lc code=start
import sys

def rotate_matrix_in_place(matrix: list[list[int]]):
    """This function contains the pure core algorithm to rotate a matrix in-place."""
    n = len(matrix)
    # 2.1 沿主对角线转置
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # 2.2 反转每一行
    for row in matrix:
        row.reverse()

def solve() -> bool:
    """
    Reads and processes one test case.
    Returns True if a case was processed, False if input has ended.

    工作流程:
    1. 首先读取第一行数据，获取矩阵维度 N。
    2. 接着循环读取 N 行，构建完整的矩阵。
    3. 调用核心算法旋转矩阵。
    4. 格式化并打印结果。
    5. 最后返回 True 表示本组数据处理成功。主循环 (`while solve()`) 收到 True 后，
       会继续调用本函数来尝试处理下一组数据。
    6. 如果读取输入时遇到文件末尾或错误，则返回 False，主循环会终止。
    """
    # 1. 读取输入 (Input Handling)
    try:
        # 读取第一行，获取矩阵维度 N
        # sys.stdin.readline() 会读入一行，包括末尾的换行符'\n'，所以用 .strip() 去掉
        #每次运行 sys.stdin.readline() 都会读取下一行输入
        #line = sys.stdin.readline() 这里会读取一行输入
        #然后会在 for 循环中 读取剩下的输入 像鼠标移动到下面，但是它永远不会回去。
        line = sys.stdin.readline()
        if not line.strip():  # If the line is empty or just whitespace, we've reached the end.
            return False
        n = int(line.strip())
        
        matrix = []
        for _ in range(n):
            # 循环读取 N 行
            # .split() 会按空格分割字符串，返回一个字符串列表
            # map(int, ...) 将列表中的每个字符串转换为整数
            row = list(map(int, sys.stdin.readline().strip().split()))
            #这个读取数据的流程是这样的。
            #sys.stdin.readline() 会读取一行输入
            #然后用 .strip() 去掉末尾的换行符
            #接着用 .split() 按空格分割字符串，返回一个字符串
            #最后用 map(int, ...) 将字符串列表转换为整数列表
            #加入说 用 第一行的输入是 1 2 3/n
            #那么首先 string.strip() 会去掉末尾的换行符，得到 "1 2 3"
            # 补充一下 sys.stdin.readline() 其实就是一个字符串
            #然后使用.split() 会将这个字符串按空格分割成 ["1", "2", "3"]
            #最后使用 map(int, ...) 将这个字符串列表转换为整数列表 [1, 2, 3]

            matrix.append(row)
            #然后将这个整数列表添加到 matrix 中
    except (IOError, ValueError):
        # If there's a parsing error or the file ends unexpectedly, stop.
        return False

    # 2. 核心算法 (Core Algorithm)
    rotate_matrix_in_place(matrix)

    # 3. 格式化输出 (Output Formatting)
    for row in matrix:
        # 将行内所有整数用 map(str, ...) 转换回字符串
        # 用 " ".join(...) 将它们用空格连接成一个字符串
        print(" ".join(map(str, row)))
        #这个效果是：比如现在有一个 [7,4,1]
        #那么 map(str, row) 会将这个列表中的每个整数转换为字符串，得到 ["7", "4", "1"]
        #然后 " ".join(...) 会将这些字符串用空格连接起来，得到 "7 4 1"
        #最后 print(...) 会输出这个字符串
    return True

# 程序主入口
if __name__ == "__main__":
    # 很多 ACM 题目可能有多个测试用例，需要用 while 循环处理
    # The loop below will call solve() repeatedly until it returns False,
    # which happens at the end of the input.
    while solve():
        pass
    # pass 在 Python 中是一个“空操作”语句。它的唯一作用就是占位，
    # 告诉解释器“这里语法上需要有一行代码，但我们什么也不用做”。它不会结束循环，也不会跳过循环。
    #但是在检查是不是true的时候，会执行solve() 函数。
    #执行完了第一组 返回 true 执行完了第二组 返回 true
    #但执行 第三组的时候line.strip() 会直接返回 false 结束循环
    #这也是前面为什么在 发现读取的字符串为空的时候 返回false 的原因。
# @lc code=end



#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]\n
# @lcpr case=end

#
