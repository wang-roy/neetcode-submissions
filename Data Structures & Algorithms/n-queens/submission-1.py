class Solution:
    def legal(self, positions: List[Tuple], n: int) -> bool:
        cols = [pos[1] for pos in positions]
        if len(set(cols)) != len(cols):
            return False
        for i in range(len(positions)):
            row1, col1 = positions[i]
            for j in range(i+1, len(positions)):
                row2, col2 = positions[j]
                if row1 - col1 == row2 - col2 or row1 + col1 == row2 + col2:
                    return False
        
        return True

    
    def convertToBoard(self, positions: List[Tuple], n: int) -> List[str]:
        board = []
        positions_set = set(positions)
        for i in range(n):
            row = ""
            for j in range(n):
                if (i, j) in positions_set:
                    row += "Q"
                else:
                    row += "."
            board.append(row)
        
        return board

    def solveNQueens(self, n: int) -> List[List[str]]:
        queue = [(0, [])]
        solutions = []

        while len(queue) > 0:
            # row = current row, positions = positions of currently placed queens
            row, positions = queue.pop(0)
            print(row)
            print(positions)
            if len(positions) == n:
                print(self.convertToBoard(positions, n))
                solutions.append(self.convertToBoard(positions, n))
                continue
            for col in range(n):
                new_positions = positions + [(row, col)]
                if self.legal(new_positions, n):
                    queue.append((row+1, new_positions))    
            
        return solutions
