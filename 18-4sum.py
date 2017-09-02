# -*- coding: utf-8 -*-

# Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target?
# Find all unique quadruplets in the array which gives the sum of target.
#
# Note: The solution set must not contain duplicate quadruplets.
#
# For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.
#
# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        return_list = []
        l = len(nums)
        nums.sort()
        for i in range(0, l - 3):
            # 去除重复计算
            if nums[i + 1] == nums[i] and i+1 < l-3:
                continue
            r = self.threeSum(nums[i + 1:], target - nums[i])
            for each in r:
                each.append(nums[i])
                return_list.append(each)
        return return_list

    def threeSum(self, nums, target):
        """
        寻找三者之和为target的结果列表
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        l = len(nums)
        r = []
        for i in range(0, l - 2):
            if (i == 0 or (i > 0 and nums[i] != nums[i - 1])) and nums[i] <= 0:
                j = i + 1
                k = l - 1
                sum = target - nums[i]
                while j < k:
                    if nums[j] + nums[k] == sum:
                        r.append([nums[i], nums[j], nums[k]])
                        while j < k and nums[j] == nums[j + 1]:
                            j += 1
                        while j < k and nums[k] == nums[k - 1]:
                            k -= 1
                        j += 1
                        k -= 1
                    elif nums[j] + nums[k] < sum:
                        j += 1
                    else:
                        k -= 1
        return r

        # l = len(nums)
        # return_list = []
        # for i in range(0, l - 2):
        #     # 去除重复计算
        #     if nums[i + 1] == nums[i] and i+1 < l-2:
        #         continue
        #     s = target - nums[i]
        #     j = i + 1
        #     k = l - 1
        #     while j < k:
        #         if nums[j] + nums[k] == s:
        #             return_list.append([nums[i], nums[j], nums[k]])
        #
        #             # 去除重复计算
        #             while j < k and nums[j + 1] == nums[j]:
        #                 j += 1
        #             while k > j and nums[k - 1] == nums[k]:
        #                 k -= 1
        #             j += 1
        #             k -= 1
        #         elif nums[i] + nums[k] < s:
        #             j += 1
        #             while j < k and nums[j + 1] == nums[j]:
        #                 j += 1
        #         else:
        #             k -= 1
        #             while k > j and nums[k - 1] == nums[k]:
        #                 k -= 1
        # return return_list


s = [1, 0, -1, 0, -2, 2]
t = 0
print Solution().fourSum(s, t)
