class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        adjMatrix = {}
        for v1, v2 in edges:
            v1AdjList = adjMatrix.get(v1, [])
            adjMatrix.update({v1: v1AdjList+[v2]})
            
            v2AdjList = adjMatrix.get(v2, [])
            adjMatrix.update({v2: v2AdjList+[v1]})

        queue=[0]
        visited = set()
        while queue:
            v1 = queue.pop(0)
            print(v1)
            adjList = adjMatrix.get(v1, [])
            for v2 in adjList:
                if v2 not in visited: 
                    queue.append(v2)
            visited.add(v1)
        print(visited)
        return len(visited) == n