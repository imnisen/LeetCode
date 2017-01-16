class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        while s:
            head = s[0]
            s = s[1:]
            swap = head
            for each in s:
                if each in swap:
                    break
                else:
                    swap += each
            if len(swap) > max_length:
                max_length = len(swap)
        return max_length

if __name__ == "__main__":
    print Solution().lengthOfLongestSubstring("abcabcbb")
