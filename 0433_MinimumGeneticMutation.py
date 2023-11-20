from typing import List
from collections import deque


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        que = deque()
        visited = set()
        que.append(startGene)
        number_of_mutation = 0

        while que:
            for _ in range(len(que)):
                gene = que.popleft()

                if gene == endGene:
                    return number_of_mutation

                if gene in visited:
                    continue

                visited.add(gene)

                for next_gene in bank:
                    if self.is_valid_mutation(gene, next_gene) and next_gene not in visited:
                        que.append(next_gene)

            number_of_mutation += 1

        return -1

    def is_valid_mutation(self, gene1, gene2):
        count = 0
        for i in range(8):
            if gene1[i] != gene2[i]:
                count += 1
        return count == 1

