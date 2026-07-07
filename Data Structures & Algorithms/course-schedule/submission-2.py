class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def getClosure(adj, i, visited=set()):
            print(f"i: {i}")
            print(f"visited: {visited}")
            if i in visited:
                return set()
            visited.add(i)
            downstream = adj[i]
            temp = set()
            for j in downstream:
                temp.update(getClosure(adj, j, visited))
            downstream.update(temp)
            return downstream

        # initialize adjacency matrix
        adj = dict([(i, set()) for i in range(numCourses)])
        
        # build adjacency matrix
        for course, prereq in prerequisites:
            adj[prereq].add(course)
        print(adj)
        for i in adj:
            x = getClosure(adj, i, set())
            print(f"closure of {i}: {x}")
            if i in x:
                return False
        return True