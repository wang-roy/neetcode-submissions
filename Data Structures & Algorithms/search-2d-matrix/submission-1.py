class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Received this problem in an interview before
        target_row = None
        left = 0
        right = len(matrix)-1
        while left <= right:
            mid_row = (left + right) // 2
            if matrix[mid_row][0] <= target and matrix[mid_row][-1] < target:
                left = mid_row+1
            elif matrix[mid_row][0] > target:
                right = mid_row-1
            else:
                target_row = mid_row
                break
        
        print(target_row)

        if target_row is None:
            return False
        
        
        
        row = matrix[target_row]
        left = 0
        right = len(row)-1
        while left <= right:
            mid = (left + right) // 2
            if row[mid] < target:
                left = mid+1
            elif row[mid] > target:
                right = mid-1
            else:
                return True
        
        return False
            
                