import heapq

class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        n = len(profits)
        projects = sorted(zip(capital, profits))  # sort by capital
        max_heap = []
        i = 0

        for _ in range(k):
            # Push all affordable projects into max-heap
            while i < n and projects[i][0] <= w:
                # max-heap by negating profit
                heapq.heappush(max_heap, -projects[i][1])
                i += 1
            
            if not max_heap:
                break  # can't afford any more projects

            # pick most profitable available project
            w += -heapq.heappop(max_heap)
        
        return w
