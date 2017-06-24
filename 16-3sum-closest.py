# -*- coding: utf-8 -*-


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        l = len(nums)
        closest_three_sum = None
        min_delta = None
        for i in range(0, l-2):
            if i == 0 or (i > 0 and nums[i] != nums[i-1]):
                j = i+1
                k = l-1

                while True:  # 模拟do 循环, 汗颜
                    three_sum = nums[i] + nums[j] + nums[k]
                    delta = three_sum - target

                    if min_delta:
                        if abs(delta) < min_delta:
                            min_delta = abs(delta)
                            closest_three_sum = three_sum
                    else:
                        min_delta = abs(delta)
                        closest_three_sum = three_sum

                    if delta == 0:
                        return target
                    elif delta > 0:
                        k -= 1
                    else:
                        j += 1

                    if j >= k:
                        break

        return closest_three_sum




print Solution().threeSumClosest([0, 0, 0], 1)