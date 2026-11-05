class Solution:
    # We want to just combine our lists sequentially and then use the binary search approach to search for the target. So we have to search through the matrix, and each element which is a list we can append 
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        combined_list = []

        for element in matrix:
            combined_list += element

        left = 0
        right = len(combined_list) - 1

        while left <= right:
            middle = left + ((right - left) // 2)

            if target  == combined_list[middle]:
                return True
            elif target > combined_list[middle]:
                left = middle + 1
            else:
                right = middle - 1

        return False
            
        