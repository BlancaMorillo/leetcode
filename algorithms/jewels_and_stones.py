// Source : https://leetcode.com/problems/jewels-and-stones/description
// Author : Blanca Morillo
// Date   : 2023-Oct-31

class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        count = 0
        jewels_array = list(jewels)

        for jewel in jewels_array:
            count += stones.count(jewel)

        return count
