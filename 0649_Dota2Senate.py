class Solution:

    def predictPartyVictory(self, senate: str) -> str:
        radiant, dire = deque(), deque()
        n = len(senate)
        for i, senator in enumerate(senate):
            if senator == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:
            if radiant[0] < dire[0]:
                radiant.append(n)
            else:
                dire.append(n)
            n += 1
            radiant.popleft(), dire.popleft()

        return 'Radiant' if radiant else 'Dire'
