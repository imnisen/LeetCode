# -*- coding: utf-8 -*-


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d_to_c = {
            '2': ['a', 'b','c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return d_to_c[digits[0]]
        r = []
        for ch in d_to_c[digits[0]]:
            for e in self.letterCombinations(digits[1:]):
                r.append(ch+e)
        return r


# print Solution().letterCombinations('23')
# print Solution().letterCombinations('')
print Solution().letterCombinations('2')