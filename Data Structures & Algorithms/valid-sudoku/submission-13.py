class Solution:
    # First we can go through each row and make sure that there are no dupes by adding each number to a set and checking if its already in the set or not. Then do the same thing but for columns we have to make a nested loop with the col being the outer loop and the row being the inner loop so that we can go throughe each number from a single column before moving on. And then lastly we have to make a row loop that only goes from 0, 3, or 6. And then inside do a col loop that only goes from 0, 3, and 6. And then we can make our set and then have another row loop that goes three times. And then have another col loop inside that also goes 3 times. And then check if the numbers are duplicates and whatsoever.
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()

            for number in row:
                if number == ".":
                    continue

                if number in seen:
                    return False

                seen.add(number)

        for col in range(9):
            seen = set()

            for row in range(9):
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
                







