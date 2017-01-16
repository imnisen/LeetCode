class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_len = len(nums)
        i = 0
        while i < num_len:
            j = i + 1
            while j < num_len:
                if nums[i] + nums[j] == target:
                    return [i, j]
                j += 1
            i += 1
        return []

    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return [lookup[target-num], i]
            lookup[num] = i
        return []




if __name__ == '__main__':
    assert Solution().twoSum2((2, 7, 11, 15), 13) == [0, 2]
    print 'Pass Test'
