from typing import List


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        answer = []
        left_sum = 0
        left_sums = []

        for num in nums:
            left_sum += num
            left_sums.append(left_sum)

        for query in queries:
            l, r = 0, len(left_sums) - 1

            while l <= r:
                middle = (l + r) // 2
                if left_sums[middle] > query:
                    r = middle
                else:
                    l = middle + 1
            answer.append(l)

        '''
         l           m               r  
        [1, 2, 3, 8, 9, 11, 25, 26, 27]
        '''

        return answer
