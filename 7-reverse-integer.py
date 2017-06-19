class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x < 0:
            s = ''
            for each in str(0 - x):
                s = each + s
            v = 0 - int(s)
        else:
            s = ''
            for each in str(x):
                s = each + s
            v = int(s)

        # pretend 32bit, so sad
        if v > 2 ** 31 - 1 or v < 0 - 2 ** 31:
            return 0
        else:
            return v
