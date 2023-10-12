from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        result = []
        for i in range(len(image)):
            result.append([1 - num for num in image[i][::-1]])

        return result
