class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        word_len = len(word)
        def dfs(i: int, j: int, visited: set) -> bool:
            idx = len(visited)
            
            # print(visited)
            # print(f"{i},{j}")
            if word[idx] == board[i][j] and (i,j) not in visited:
                visited.add((i, j))
                if idx == word_len-1:
                    return True
                
                match = False
                
                if i < m-1:
                    match = match or dfs(i+1, j, visited.copy())
                
                if i >= 1:
                    match = match or dfs(i-1, j, visited.copy())
                
                if j >= 1:
                    match = match or dfs(i, j-1, visited.copy())
                
                if j < n-1:
                    match = match or dfs(i, j+1, visited.copy())

                return match
            return False
        for i in range(m):
            for j in range(n):
                if dfs(i, j, set()):
                    return True
        return False
        
        

        