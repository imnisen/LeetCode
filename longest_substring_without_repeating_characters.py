# -*- coding: utf-8 -*-


class Solution(object):
    # Not good than below
    # def lengthOfLongestSubstring(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     max_length = 0
    #     while s:
    #         head = s[0]
    #         s = s[1:]
    #         swap = head
    #         for each in s:
    #             if each in swap:
    #                 break
    #             else:
    #                 swap += each
    #         if len(swap) > max_length:
    #             max_length = len(swap)
    #     return max_length

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        while s:
            swap = set()  # set() is faster than string search
            for each in s:
                if each in swap:
                    break
                else:
                    swap.add(each)
            if len(swap) > max_length:
                max_length = len(swap)
            s = s[1:]
        return max_length

    def lengthOfLongestSubstring2(self, s):
        """
        这个方法区别于上个方法的地方在于,
        对应字符串'abcabcbb'来说, 当找到'abca'重复时, 记下此时的max_length后,
        上一种方法从'bcabcbb'再开始寻找,
        而这一种方法从'abcbb'开始寻找.
        :type s: str
        :rtype: int
        """
        max_length = 0
        while s:
            swap = set()  # set() is faster than string search
            break_index = 0
            for i, each in enumerate(s):
                if each in swap:
                    break_index = i
                    break
                else:
                    swap.add(each)
            if len(swap) > max_length:
                max_length = len(swap)
            if break_index != 0:
                s = s[break_index:]
            else:
                s = []
        return max_length

if __name__ == "__main__":
    assert Solution().lengthOfLongestSubstring2("abcabcbb") == 3
    assert Solution().lengthOfLongestSubstring2("bbbbb") == 1
    assert Solution().lengthOfLongestSubstring2("pwwkew") == 3
