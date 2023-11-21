from typing import List
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        que = deque()
        que.append(beginWord)
        word_list = set(wordList)
        level = 1

        while que:
            for _ in range(len(que)):
                world = que.popleft()

                if world == endWord:
                    return level

                if world != beginWord and world not in word_list:
                    continue

                word_list.discard(world)

                for next_word in word_list:
                    if self.is_valid_world(world, next_word):
                        que.append(next_word)

            level += 1
        return 0

    def is_valid_world(self, word1, word2):
        count = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                count += 1
                if count >= 2:
                    return False

        return True
