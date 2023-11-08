// Source : https://leetcode.com/problems/longest-common-prefix/description/
// Author : Blanca Morillo
// Date   : 2023-Nov-7


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        min_str = min(strs, key=len)
        print(min_str)
        temp = ""

        for idx, letter in enumerate(min_str):
            for word in strs:
                if word[idx] != letter:
                    return temp
            temp += letter
        return temp
