// Source : https://leetcode.com/problems/shuffle-the-array/description/
// Author : Blanca Morillo
// Date   : 2023-Nov-1

class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        
        shuffled_array = []
        for i in range(n):
            shuffled_array.append(nums[i])
            shuffled_array.append(nums[i+n])
        return shuffled_array