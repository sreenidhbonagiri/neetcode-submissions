class Solution:
    # We want to just combine our lists sequentially and then use the binary search approach to search for the target. So we have to search through the matrix, and each element which is a list we can append 
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        col = len(matrix[0])

        left = 0
        right = (rows * col) - 1

        while left <= right:
            middle = left + ((right - left) // 2)
            ro = middle // col
            co = middle % col

            if target  == matrix[ro][co]:
                return True
            elif target > matrix[ro][co]:
                left = middle + 1
            else:
                right = middle - 1

        return False
            
        