// Source : https://leetcode.com/problems/concatenation-of-array/description
// Author : Blanca Morillo
// Date   : 2023-Nov-8
class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = nums[:]
        for num in nums:
            res.append(num)
        return res
