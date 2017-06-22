# -*- coding: utf-8 -*-

# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
#
# The matching should cover the entire input string (not partial).
#
# The function prototype should be:
# bool isMatch(const char *s, const char *p)
#
# Some examples:
# isMatch("aa","a") → false
# isMatch("aa","aa") → true
# isMatch("aaa","aa") → false
# isMatch("aa", "a*") → true
# isMatch("aa", ".*") → true
# isMatch("ab", ".*") → true
# isMatch("aab", "c*a*b") → true
# isMatch("baccbbcbcacacbbc", "c*.*b*c*ba*b*b*.a*") → true


# # Solution1
# class Solution(object):
#     """
#     leetcode时间超时
#     用p[j:j+1]这样来取p[j]的元素是因为防止index out of range
#     """
#     def isMatch(self, s, p):
#         """
#         :type s: str
#         :type p: str
#         :rtype: bool
#         """
#
#         return self.helper(s, p, 0, 0)
#
#     def helper(self, s, p, i, j):
#         if j == len(p):
#             return i == len(s)
#
#         if p[j + 1:j+2] != '*':
#             if s[i:i+1] == p[j:j+1] or p[j:j+1] == '.' and i < len(s):
#                 return self.helper(s, p, i + 1, j + 1)
#             else:
#                 return False
#
#         while i < len(s) and (p[j:j+1] == '.' or s[i:i+1] == p[j:j+1]):
#             if self.helper(s, p, i, j + 2):
#                 return True
#             i += 1
#         return self.helper(s, p, i, j + 2)


