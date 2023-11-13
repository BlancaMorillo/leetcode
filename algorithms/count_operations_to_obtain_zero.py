// Source: https://leetcode.com/problems/count-operations-to-obtain-zero/description/
// Author: Blanca Morillo
// Date: 2023-Nov-12

class Solution(object):
    def countOperations(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        temp_1 = num1
        temp_2 = num2
        count = 0
        while temp_1 != 0 and temp_2 != 0:
            if temp_1 >= temp_2:
                temp_1 -= temp_2
                count += 1
            else:
                temp_2 -= temp_1
                count += 1
        return count
