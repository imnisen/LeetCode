# -*- coding: utf-8 -*-

# 超耗时的方案
# class Solution(object):
#     def maxArea(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         line_num = len(height)
#         max_area = 0
#         for i in range(line_num):
#             for j in range(i+1, line_num):
#                 area = min(height[i],height[j]) * (j-i)
#                 if area > max_area:
#                     max_area = area
#         return max_area

# 再考虑这个问题, 可以发现下面的特点
# 从宽度最大的容器开始计算(即一首一尾两根直线, 假设高度为h1,hn), 其它容器的面积如果想要比这个最大宽度的容器要面积大,
# 在宽度更小的情况下,想必高度要更高,假设两个高度为hx,hy, 即 min(hx,hy) > min(h1,hn) 的, 即:hx>min(h1,hn) and hy>min(h1,hn)
# 所以 两边各自向内收缩, 直到各自找到比min(h1,hn)要大的直线, 这种情况下,才有可能面积比最大宽度的大
# 比较完后, 在重复这个过程, 直到收缩到首尾重合

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        i = 0
        j = len(height) - 1
        while i < j:
            h = min(height[i], height[j])
            max_area = max(max_area, (j - i) * h)
            while height[i] <= h and i < j:
                i += 1
            while height[j] <= h and i < j:
                j -= 1
        return max_area
