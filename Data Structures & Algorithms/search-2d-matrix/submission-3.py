class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_length = len(matrix)
        col_length = len(matrix[0])
        
        left = 0
        right = (row_length * col_length) - 1

        while left <= right:
            middle = left + (right - left) // 2
            row = middle // col_length
            col = middle % col_length

            if target == matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                left = middle + 1
            else:
                right = middle - 1

        return False
