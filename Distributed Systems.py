import collections
import heapq

# analysis
# T = O(Elog(V))
# S = O(Elog(V))

class Solution:
    def solve(self, n, edges):
        # the advantage of using collections.defaultdisct(list)
        # is that we don't need to check for membership.
        # if something doesn't exist, it will automatically be initialized
        adjacency_list_with_weights = collections.defaultdict(list)

        for start, end, weight in edges:
            adjacency_list_with_weights[start].append((end, weight))
            adjacency_list_with_weights[end].append((start, weight))

        # in a minHeap, if you store a tuple, the minimum property
        # of the heap applies to the first element in that tuple
        # here it applies to the weight
        minHeap = [(0, 0)] # holds (weight, node)
        # initialized to (0, 0) because we are told that we start from
        # 0 and the time spent to get from 0 to itself is 0

        visited = set()
        time = 0

        while minHeap:
            weight, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)

            time = max(time, weight)

            for neighbor, neighborWeight in adjacency_list_with_weights[node]:
                if neighbor not in visited:
                    heapq.heappush(minHeap, (weight + neighborWeight, neighbor))

        return time




