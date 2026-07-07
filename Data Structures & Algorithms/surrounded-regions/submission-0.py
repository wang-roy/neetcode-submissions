class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def bfs(board, i, j, visited):
            group = []
            queue = [(i, j)]
            while queue:
                x, y = queue.pop(0)
                group.append((x, y))
                visited.add((x, y))
                if (x, y - 1) not in visited and y - 1 >= 0 and board[x][y-1] == 'O':
                    queue.append((x, y - 1))
                if (x, y + 1) not in visited and y + 1 < len(board[0]) and board[x][y+1] == 'O':
                    queue.append((x, y + 1))
                    
                if (x - 1, y) not in visited and x - 1 >= 0 and board[x-1][y] == 'O':
                    queue.append((x - 1, y))
                if (x + 1, y) not in visited and x + 1 < len(board) and board[x+1][y] == 'O':
                    queue.append((x + 1, y))
            return group, visited
        
        def isSurrounded(board, group):
            for i, j in group:
                if i == 0 or i == len(board)-1 or j == 0 or j == len(board[0])-1:
                    return False
            return True
        visitedO_s = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and (i, j) not in visitedO_s:
                    visitedO_s.add((i, j))
                    print(visitedO_s)
                    group, visitedO_s = bfs(board, i, j, visitedO_s)
                    print(group)
                    print(visitedO_s)
                    if isSurrounded(board, group):
                        for x, y in group:
                            board[x][y] = 'X'
                    


