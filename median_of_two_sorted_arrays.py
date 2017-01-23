# -*- coding: utf-8 -*-


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        arr = []
        #  依次从两个列表拿出一个, 比较大小, 小的加到数组
        while nums1 or nums2:
            if not nums1:
                arr.extend(nums2)
                break
            if not nums2:
                arr.extend(nums1)
                break

            p = nums1.pop(0)
            q = nums2.pop(0)

            if p < q:
                arr.append(p)
            else:
                arr.append(q)

        # now arr has all sorted data
        arr_len = len(arr)
        if arr_len % 2 == 0:
            median = (arr[arr_len / 2 - 1] + arr[arr_len / 2]) / 2.0
        else:
            median = arr[arr_len / 2] * 1.0
        return median

if __name__ == "__main__":
    print Solution().findMedianSortedArrays([1, 3, 5, 7], [2, 4, 6])
    print Solution().findMedianSortedArrays([1, 3, 5], [2, 4, 6])

