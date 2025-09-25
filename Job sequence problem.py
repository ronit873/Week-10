class Solution:
    def jobSequencing(self, deadline, profit):
        import heapq
        pairs = sorted(zip(deadline, profit), key=lambda x: (x[0], -x[1]))
        h, cur = [], 0
        for d, p in pairs:
            if d > cur:
                cur += 1
                heapq.heappush(h, p)
            elif d == cur:
                heapq.heappushpop(h, p)
        return len(h), sum(h)