# -*- coding: utf-8 -*-

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x != 0 and x % 10 == 0):  # 当x为复数或者x是10的倍数(除了0外),都不是回文
            return False
        else:
            tmp = 0
            while x > tmp:
                tmp = tmp * 10 + x % 10
                x /= 10
            return x == tmp or x == tmp / 10

print Solution().isPalindrome(123323321)
print Solution().isPalindrome(1233233211)
print Solution().isPalindrome(-1)
print Solution().isPalindrome(1)
