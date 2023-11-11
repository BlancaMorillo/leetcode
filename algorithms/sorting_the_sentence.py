// Source: https://leetcode.com/problems/sorting-the-sentence/description/
// Author: Blanca Morillo
// Date: 2023-11-11
class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """

        array = s.split()
        res = [None] * len(array)

        for word in array:
            index_res = int(word[-1]) - 1
            res[index_res] = word[0:-1]

        return ' '.join(res)
