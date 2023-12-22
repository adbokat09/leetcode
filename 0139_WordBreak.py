from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        n = len(s)
        spase_of_str = [0] * n
        for i in range(n):
            if s[:i + 1] in wordDict:
                spase_of_str[i] = 1
            else:
                for j in range(i):
                    if spase_of_str[j] == 1 and s[j + 1:i + 1] in wordDict:
                        spase_of_str[i] = 1

        return spase_of_str[-1] == 1



print(Solution().wordBreak("leetcode", ["leet","code"]))
