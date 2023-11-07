// Source : https://leetcode.com/problems/palindrome-number/description/
// Author : Blanca Morillo
// Date   : 2023-Nov-7

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Solution 1 - Runtime 36ms Memory 13.47 MB
        # if x < 0 :
        #     return False
        # elif x < 10:
        #     return True
        # else:
        #     x_str = str(x)
        #     return x_str == x_str[::-1]

        # Solution 2 - Runtime 27ms Memory 13.24 MB
        if x < 0:
            return False
        elif x < 10:
            return True
        else:
            x_str = str(x)
            length = len(x_str)
            for i in range(length // 2):
                if x_str[i] != x_str[length - i - 1]:
                    return False
            return True
