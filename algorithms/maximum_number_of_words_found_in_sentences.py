// Source : https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/description/
// Author : Blanca Morillo
// Date   : 2023-Nov-14

class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        result = 0
        for sentence in sentences:
            word_count = len(sentence.split())
            if word_count > result:
                result = word_count
        return result
