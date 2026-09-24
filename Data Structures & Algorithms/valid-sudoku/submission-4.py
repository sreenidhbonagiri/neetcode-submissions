class Solution:
    #We can loop through each list in the big list, and check if each number is unique or not by seeing if its in the set or not. So loop through each list, then loop through each element in each list, and then keep adding those elements into the set and check if its already in the set or not. If not, then we the rows are valid if the number is already seen in the set then we can just return false right away
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()

            for number in row:
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
        
        for start_row in [0, 3, 6]:
            for start_col in [0, 3, 6]:
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







