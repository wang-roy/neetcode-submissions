class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_matrix = {}
        for u, v, t in times:
            if u not in adj_matrix:
                adj_matrix.update({u: [(v, t)]})
            else:
                adj_matrix[u].append((v, t))
        print(adj_matrix)
        dist = [math.inf] * n
        dist[k-1] = 0
        queue = [(k, 0)]
        while len(queue) > 0:
            curr, time = queue.pop(0)
            if time <= dist[curr-1]:
                dist[curr-1] = time
                if curr in adj_matrix:
                    for v, t in adj_matrix[curr]:
                        queue.append((v, time+t))
            print((curr, time))
            print(dist)
        min_time = max(dist)
        if min_time == math.inf:
            return -1
        return min_time
            

                


        