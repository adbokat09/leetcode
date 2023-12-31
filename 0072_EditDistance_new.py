from functools import cache


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def dp(word1, word2):
            if not word1 or not word2:
                return max(len(word1), len(word2))

            if word1[0] == word2[0]:
                return dp(word1[1:], word2[1:])

            return min(
                dp(word1[1:], word2),
                dp(word1[1:], word2[1:]),
                dp(word1, word2[1:])
            ) + 1

        return dp(word1, word2)
'''
makaka
table

                    makaka - table
    akaka - table    takaka - table    tmakaka - table 
                                


'''
