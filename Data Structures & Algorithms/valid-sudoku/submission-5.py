class Solution:
    #
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()
            for i in range(len(row)):
                number = row[i]
                
                if number == ".":
                    continue

                if number in seen:
                    return False
                
                seen.add(number)

        for col in range(len(board)):
            seen = set()

            for row in range(len(board)):
                number = board[row][col]

                if number == ".":
                    continue
    
                if number in seen:
                    return False

                seen.add(number)

        for start_row in [0,3,6]:
            for start_col in [0,3,6]:
                seen = set()

                for row in range(3):
                    for col in range(3):
                        number = board[start_row + row][start_col + col]

                        if number == ".":
                            continue
    
                        if number in seen:
                            return False

                        seen.add(number)

        return True



        






