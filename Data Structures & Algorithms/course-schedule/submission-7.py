class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def find_leaf(adj):
            for i in adj:
                if len(adj[i]) == 0:
                    return i
            return None
        # initialize adjacency matrix
        reverse_adj = dict([(i, set()) for i in range(numCourses)])
        adj = dict([(i, set()) for i in range(numCourses)])
        # build adjacency matrix
        for course, prereq in prerequisites:
            # catch degenerate cycle case
            if course == prereq:
                return False
            adj[prereq].add(course)
            reverse_adj[course].add(prereq)
        print(adj)
        print(reverse_adj)

        # start a leaf node, removing connections pointing to that leaf node to reveal more leaves
        
        visited = set()
        leaf_node = find_leaf(adj)
        
        while leaf_node not in visited and leaf_node != None:
            print(f"leaf node: {leaf_node}")
            print(f"adj: {adj}")
            print(f"reverse_adj: {reverse_adj}")
            # remove edges pointing to this leaf (from both adj and reverse adj lists) to expose more leaves
            for i in reverse_adj[leaf_node]:
                adj[i].remove(leaf_node)
            reverse_adj[leaf_node] = set()
            # remove the leaf from consideration
            adj.pop(leaf_node)
            # tick counter
            visited.add(leaf_node)
            leaf_node = find_leaf(adj)
        
        # if can't find a new leaf and haven't traversed the whole tree, there's a cycle.
        return len(visited) == numCourses
        # return True