# -*- coding: utf-8 -*-


class Solution(object):
    def special_case(self, s):
        s1 = ''
        s2 = ''
        for index, each in enumerate(s):
            if index % 2 == 0:
                s1 += each
            else:
                s2 += each
        return s1 + s2

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # 特殊情况处理
        if len(s) <= numRows:
            return s
        elif numRows == 1:
            return s
        elif numRows == 2:
            return self.special_case(s)
        else:
            s_lst = self.split_string(s, numRows)
            s_converted = ''
            for i in range(numRows):
                # 第0,2,4,...列取第i个元素
                # 第1,3,5,...列取(numRows-1)-i-1个元素; 这里的(numRows-1)-i-1是通过举例归纳出来的
                # 注意判断当每列的元素个数少于index元素的情况
                for index, each_s in enumerate(s_lst):
                    if index % 2 == 0:
                        if len(each_s)-1 < i:
                            pass
                        else:
                            s_converted += each_s[i]
                    else:
                        if len(each_s) - 1 < (numRows-1)-i-1:
                            pass
                        else:
                            if (numRows-1)-i-1 < 0:
                                pass
                            else:
                                s_converted += each_s[(numRows-1)-i-1]
            return s_converted

    def split_string(self, s, numRows):
        """
        将一个字符串,划分成 ['numRows长度', 'numRows-2长度', 'numRows长度', 'numRows-2长度' ...]
        :param s:
        :param numRows:
        :return:
        """
        s_len = len(s)
        n = 2*numRows-2
        s1_splited = [s[i*n:(i+1)*n] for i in range(s_len/n + 1)]
        s_lst = []
        for each in s1_splited:
            s_lst.append(each[:numRows])
            s_lst.append(each[numRows:])
        return s_lst

# Solution().split_string('PAYPALISHIRING', 3)
Solution().convert('PAYPALISHIRING', 2)
