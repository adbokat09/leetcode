class RecentCounter:

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while t - self.queue[0] > 3000:
            self.queue.popleft()
        return len(self.queue)
