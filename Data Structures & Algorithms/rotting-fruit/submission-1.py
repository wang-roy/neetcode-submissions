class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def addNeighborsHelper(grid, i, j, visited, path_length):
            m = len(grid)
            n = len(grid[0])
            one_neighbors = []
            if i + 1 < m and grid[i+1][j] == 1 and (i + 1, j) not in visited:
                one_neighbors.append(((i+1, j), path_length + 1))
            if i - 1 >= 0 and grid[i-1][j] == 1 and (i - 1, j) not in visited:
                one_neighbors.append(((i-1, j), path_length + 1))
            if j + 1 < n and grid[i][j+1] == 1 and (i, j + 1) not in visited:
                one_neighbors.append(((i, j+1), path_length + 1))
            if j - 1 >= 0 and grid[i][j-1] == 1 and (i, j - 1) not in visited:
                one_neighbors.append(((i, j-1), path_length + 1))
            return one_neighbors

        distance_dict = {} # intialize distance dictionary with -1s for indices of fresh fruit (1s)
        queue = [] 
        # initialize queue with the rotten fruits (2s)
        for i in range(len(grid)): # rows
            for j in range(len(grid[0])): # cols
                if grid[i][j] == 1:
                    distance_dict.update({(i, j): float('inf')})
                elif grid[i][j] == 2:
                    queue.append(((i, j), 0))
        visited = set()
        while len(queue) > 0:
            (i, j), path_length = queue.pop(0)
            visited.add((i, j))
            if distance_dict.get((i, j)) is not None:
                if distance_dict[(i, j)] > path_length or distance_dict[(i, j)] == float('inf'):
                    distance_dict.update({(i, j): path_length})

            queue.extend(addNeighborsHelper(grid, i, j, visited, path_length))
        
        minTime = max(distance_dict.values()) if distance_dict else 0
        if minTime == float('inf'):
            minTime = -1
        return minTime
        


