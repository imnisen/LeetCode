# -*- coding: utf-8 -*-

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 从长到短开始识别, 一旦识别到就不再识别
        s_len = len(s)

        for i in range(s_len):
            if i == 0:
                if self.is_palindrome(s):
                    return s
            else:
                for j in range(i+1):
                    if i - j == 0:
                        if self.is_palindrome(s[j:]):
                            return s[j:]
                    elif self.is_palindrome(s[j:-(i-j)]):
                        return s[j:-(i-j)]
        return ''

    def is_palindrome(self, s):
        """
        检查给出的字符串是不是回文
        :param s:
        :return: True or False
        """
        s_len = len(s)
        if s_len % 2 == 0:
            s_left_part = s[:s_len/2]
            s_right_part = s[s_len/2:][::-1]
            if s_left_part == s_right_part:
                palindromic = True
            else:
                palindromic = False
        else:
            s_left_part = s[:(s_len-1)/2]
            s_right_part = s[(s_len+1)/2:][::-1]
            if s_left_part == s_right_part:
                palindromic = True
            else:
                palindromic = False
        return palindromic

if __name__ == "__main__":
    print Solution().longestPalindrome("abcda")
