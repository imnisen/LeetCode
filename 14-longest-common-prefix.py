# -*- coding: utf-8 -*-

# Solution1
# def find_longest_common_prefix(str1, str2):
#     if str1 and str2:
#         common_prefix = ''
#         str1_len = len(str1)
#         str2_len = len(str2)
#         for i in range(str1_len):
#             if i == str2_len:
#                 break
#             elif str1[i] == str2[i]:
#                 common_prefix += str1[i]
#             else:
#                 break
#     else:
#         common_prefix = ''
#     return common_prefix
#
# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#         if strs:
#             return reduce(find_longest_common_prefix, strs)
#         else:
#             return ''


def find_longest_common_prefix(str1, str2):
    common_prefix = ''
    str1_len = len(str1)
    str2_len = len(str2)
    for i in range(str1_len):
        if i == str2_len:
            break
        elif str1[i] == str2[i]:
            common_prefix += str1[i]
        else:
            break
    return common_prefix


# Sulution2 , 当其中出现一个空字符,直接停止
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs:
            str1 = strs[0]
            for each_str in strs[1:]:
                if each_str:
                    str1 = find_longest_common_prefix(str1, each_str)
                    if str1:
                        continue
                    else:
                        return ''
                else:
                    return ''
            return str1
        else:
            return ''

print Solution().longestCommonPrefix(['abcdd', 'abcd', 'abbb', 'abcef'])

