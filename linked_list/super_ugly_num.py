import heapq

class Solution:
    def nthSuperUglyNumber(self, n, primes):
        # Initialize the heap with the first super ugly number
        heap = [1]
        seen = {1}
        for _ in range(n - 1):
            # Pop the smallest number from the heap
            current = heapq.heappop(heap)
            # Generate new numbers by multiplying with each prime
            for prime in primes:
                new_number = current * prime
                if new_number not in seen:
                    seen.add(new_number)
                    heapq.heappush(heap, new_number)
        # The nth super ugly number is the smallest number in the heap
        return heapq.heappop(heap)
