#
# @lc app=leetcode.cn id=125 lang=python3
# @lcpr version=30201
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    #指针方法 双指针
    #判断是不是回文串
    #第一步是对字符串进行预处理。
        #1.遍历字符串 判断是不是字母或者数字
        #2.将遍历好的字符串 转化为小写，存在一个新的列表中。
    #第二部对处理好的文字进行双指针遍历。查看他们是不是回文串，是的话返回 true，否则返回False
        #一左一右两个指针 相向而行
        #如果有不一样的 返回false
        #如果OK，返回True
    def isPalindrome(self, s: str) -> bool:
        sb = []
        for c in s:
            if c.isalnum():
                sb.append(c.lower())
        
        s = ''.join(sb)
        left, right = 0, len(s) - 1
        while left < right:
            if s[left]!= s[right]:
                return False
            left += 1
            right -= 1
        return True 


        
        
# @lc code=end



#
# @lcpr case=start
# "A man, a plan, a canal: Panama"\n
# @lcpr case=end

# @lcpr case=start
# "race a car"\n
# @lcpr case=end

# @lcpr case=start
# " "\n
# @lcpr case=end

#

